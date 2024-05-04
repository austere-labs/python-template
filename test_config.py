from config import Config


def test_config_port():
    config = Config()
    assert config.port == "8081"
    assert config.gcp_project_id == "482777410016"
    assert (
        config.test_secret_key
        == "projects/482777410016/secrets/TestSecretForTests/versions/1"
    )
