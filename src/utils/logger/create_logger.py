from base64 import b64encode
from dataclasses import asdict, is_dataclass
from decimal import Decimal
from gzip import compress
from logging import DEBUG

from aws_lambda_powertools import Logger
from boto3.dynamodb.conditions import AttributeBase, ConditionBase


def custom_default(obj):
    if isinstance(obj, set):
        return {"type": str(type(obj)), "value": list(obj)}
    if isinstance(obj, Decimal):
        return num if (num := int(obj)) == obj else float(str(obj))
    if isinstance(obj, bytes):
        return {
            "type": str(type(obj)),
            "detail": "compress by gzip and base64 encode",
            "value": b64encode(compress(obj, 9)).decode(),
        }
    if is_dataclass(obj):
        # dataclassとして定義したクラスも is_dataclassに引っかかる
        # 引っかかるが、asdict()に渡すとエラーになる
        if isinstance(obj, type):
            return str(obj)
        else:
            return asdict(obj)
    if isinstance(obj, AttributeBase):
        return obj.name
    if isinstance(obj, ConditionBase):
        return obj.get_expression()
    try:
        return {"type": str(type(obj)), "value": str(obj)}
    except Exception as e:
        return {
            "type": str(type(obj)),
            "detail": "failed to convert to string",
            "error": {"type": str(type(obj)), "value": str(e)},
        }


def create_logger(name: str) -> Logger:
    return Logger(
        service=name, level=DEBUG, use_rfc3339=True, json_default=custom_default
    )
