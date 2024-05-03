from dotenv import load_dotenv
import os


class Config:
    load_dotenv()

    def __init__(self) -> None:
        self.port = os.getenv("PORT")
