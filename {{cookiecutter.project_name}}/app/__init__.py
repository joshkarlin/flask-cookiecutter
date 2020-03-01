from flask import Flask
from redis import Redis
from rq import Queue

from app.config import get_config_class


def create_app() -> Flask:
    """Creates a flask app, sets up config and registers required add-ons."""
    app = Flask(__name__)
    app.config.from_object(get_config_class())

    # Setup redis and rq
    app.redis = Redis.from_url(app.config["REDIS_URL"])
    app.task_queue = Queue("default", connection=app.redis)

    return app
