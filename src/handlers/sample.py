from dataclasses import dataclass

from utils.dataclasses import load_environments
from utils.logger import create_logger, logging_handler


@dataclass(frozen=True)
class EnvironmentVariables:
    system_name: str


logger = create_logger(__name__)


@logging_handler(logger)
def handler(event, context):
    env = load_environments(class_dataclass=EnvironmentVariables)
    logger.info("call", data={"env": env})
    return env
