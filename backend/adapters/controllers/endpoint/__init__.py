from sanic.blueprints import Blueprint

from backend.adapters.controllers.endpoint.api import api_endpoint

endpoint = Blueprint.group(api_endpoint)
