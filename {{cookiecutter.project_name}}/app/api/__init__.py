from flask import Blueprint
from flask_restx import Api

from app.api.namespaces import dummy_task_namespace

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    api_blueprint,
    version="1.0",
    title="{{cookiecutter.project_name}} API",
    description="A simple API",
)
api.add_namespace(dummy_task_namespace)
