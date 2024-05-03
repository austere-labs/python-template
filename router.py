from fastapi import APIRouter, Depends
from log_config import LoggingConfig
import logging

routes = APIRouter()
log_config = LoggingConfig(log_level=logging.INFO)


@routes.get("/")
async def welcome(logger: logging.Logger = Depends(log_config.get_logger)):
    logger.info("Welcome endpoint hit!")
    return {"message": "Welcome to template API service!"}
