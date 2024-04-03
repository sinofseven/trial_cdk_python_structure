from datetime import datetime, timezone
from functools import wraps
from typing import Callable
from uuid import uuid4

from aws_lambda_powertools import Logger


def logging_function(
    logger: Logger,
    *,
    is_write: bool = True,
    with_args: bool = True,
    with_return: bool = True,
) -> Callable:
    def factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            name_function = func.__name__
            id_call = str(uuid4())
            dt_start = datetime.now(tz=timezone.utc)
            result = None
            is_error = False
            try:
                data_start = {}
                if with_args:
                    data_start["args"] = args
                    data_start["kwargs"] = kwargs
                if is_write:
                    logger.debug(
                        f'start function "{name_function}" ({id_call})', data=data_start
                    )
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.debug(
                    f'error occurred in function "{name_function}": [{type(e)}] {e}',
                    exc_info=True,
                    data={"args": args, "kwargs": kwargs},
                )
                is_error = True
                raise
            finally:
                duration = datetime.now(tz=timezone.utc) - dt_start
                data_end = {
                    "duration": {
                        "text": str(duration),
                        "total_seconds": duration.total_seconds(),
                    }
                }
                if with_return:
                    data_end["return"] = result
                if is_write or is_error:
                    status = "failed" if is_error else "succeeded"
                    logger.debug(
                        f'{status} function "{name_function}" ({id_call})',
                        data=data_end,
                    )

        return wrapper_function

    return factory
