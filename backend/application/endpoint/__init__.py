from sanic.blueprints import Blueprint

from backend.application.endpoint.api import api_endpoint

endpoint = Blueprint.group(api_endpoint)
