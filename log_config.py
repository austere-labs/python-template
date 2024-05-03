import logging
import sys
from pythonjsonlogger import jsonlogger


class LoggingConfig:
    def __init__(self, log_level: str, name="template-service"):
        self.logger_name = name
        self.log_level = log_level

    async def get_logger(self):
        # Create a custom logger
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.log_level)
        # create handler for logging to stdout
        stdoutHandler = logging.StreamHandler(stream=sys.stdout)

        stdoutHandler.setLevel(self.log_level)
        fmt = jsonlogger.JsonFormatter(
            "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
            rename_fields={"levelname": "severity", "asctime": "timestamp"},
        )
        stdoutHandler.setFormatter(fmt)
        logger.addHandler(stdoutHandler)

        yield logger
