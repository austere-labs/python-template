from dotenv import load_dotenv
import os


class Config:
    load_dotenv()

    def __init__(self) -> None:
        self.port = os.getenv("PORT")
        self.gcp_project_id = os.getenv("GCP_PROJECT_ID")
        self.test_secret_key = os.getenv("TEST_SECRET_KEY")
