from os import getenv
from pathlib import Path

class Config(object):
    REDIS_URL = getenv("REDIS_URL", "redis://")
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'
    RESTPLUS_MASK_SWAGGER = False
    APPLICATION_ROOT = Path(__file__).parent.parent.absolute()


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def get_config_class() -> Config:
    """
    Based on the value of the environment variable CONFIG_CLASS, return the appropriate
    config class.
    """
    config_mapping = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig
    }
    return config_mapping.get(getenv("FLASK_ENV"), ProductionConfig)
