from google.cloud import secretmanager

# for this dependency to work, you need to install the google-cloud-secret-manager package
# pip install google-cloud-secret-manager
# also for additional documentation you can visit
# https://cloud.google.com/secret-manager/docs/reference/libraries


class SecretManager:
    def __init__(
        self, project_id: str, gcp_client: secretmanager.SecretManagerServiceClient
    ) -> None:
        self.project_id = project_id
        self.gcp_client = gcp_client

    def get_secret(self, secret_name: str) -> str:
        response = self.gcp_client.access_secret_version(request={"name": secret_name})
        return response.payload.data.decode("UTF-8")
