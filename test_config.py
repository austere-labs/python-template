from config import Config


def test_config_port():
    config = Config()
    assert config.port == "8081"
