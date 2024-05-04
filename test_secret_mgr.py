from google.cloud import secretmanager
from secret_mgr import SecretManager
from config import Config


def test_get_secret():
    config = Config()
    gcp_project_id = config.gcp_project_id
    secret_key = config.test_secret_key
    client = secretmanager.SecretManagerServiceClient()
    gcp_sm = SecretManager(gcp_project_id, client)
    secret = gcp_sm.get_secret(secret_key)
    assert secret == "GeminiAndGPT"
