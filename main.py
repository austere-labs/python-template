from fastapi import FastAPI
from router import router
import uvicorn
from config import Config
from log_config import LoggingConfig
import logging

app = FastAPI()
app.include_router(router)

log_config = LoggingConfig(log_level=logging.INFO)
logger = log_config.get_logger()


def main():
    config = Config()
    logger.info(f"Starting indicators service on port {config.port}...")
    uvicorn.run("main:app", host="0.0.0.0", port=int(config.port))


if __name__ == "__main__":
    main()
