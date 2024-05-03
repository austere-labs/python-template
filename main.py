from fastapi import FastAPI
from router import router
import logging
import sys
from pythonjsonlogger import jsonlogger
import uvicorn
from config import Config

app = FastAPI()
app.include_router(router)


def main():
    # Setup logging
    logger = logging.getLogger("indicators-service")
    logger.setLevel(logging.DEBUG)
    # create handler for logging to stdout
    stdoutHandler = logging.StreamHandler(stream=sys.stdout)

    stdoutHandler.setLevel(logging.DEBUG)
    fmt = jsonlogger.JsonFormatter(
        "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
        rename_fields={"levelname": "severity", "asctime": "timestamp"},
    )
    stdoutHandler.setFormatter(fmt)
    logger.addHandler(stdoutHandler)
    logger.info("Starting indicators service...")

    config = Config()
    print(config.port)
    uvicorn.run("main:app", host="0.0.0.0", port=int(config.port))


if __name__ == "__main__":
    main()
