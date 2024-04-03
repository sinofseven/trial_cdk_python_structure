import os
from functools import wraps
from typing import Callable

from aws_lambda_powertools import Logger

EXCLUDE_ENV_KEYS = {
    "AWS_ACCESS_KEY_ID",
    "AWS_LAMBDA_LOG_GROUP_NAME",
    "AWS_LAMBDA_LOG_STREAM_NAME",
    "AWS_LAMBDA_RUNTIME_API",
    "AWS_SECRET_ACCESS_KEY",
    "AWS_SESSION_TOKEN",
    "AWS_SESSION_TOKEN",
    "AWS_XRAY_CONTEXT_MISSING",
    "AWS_XRAY_DAEMON_ADDRESS",
    "_AWS_XRAY_DAEMON_ADDRESS",
    "_AWS_XRAY_DAEMON_PORT",
}


def logging_handler(logger: Logger, *, with_return: bool = False) -> Callable:
    def factory(handler: Callable) -> Callable:
        @wraps(handler)
        @logger.inject_lambda_context()
        def wrapper_handler(event, context, *args, **kwargs):
            logger.debug(
                "event and environment variables",
                data={
                    "event": event,
                    "env": {
                        k: os.getenv(k)
                        for k in sorted(os.environ.keys())
                        if k not in EXCLUDE_ENV_KEYS
                    },
                },
            )

            try:
                result = handler(event, context, *args, **kwargs)
                if with_return:
                    logger.debug("handler return", data={"return": result})
                return result
            except Exception as e:
                logger.error(
                    f"error occurred in handler: [{type(e)}] {e}", exc_info=True
                )
                raise

        return wrapper_handler

    return factory
