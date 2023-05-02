from flask import Blueprint
from flask_restx import Api
from .pw_raw import ns as TestNamespace


blueprint = Blueprint(
  'api',
  __name__,
  url_prefix='/api'
)

api = Api(
  blueprint,
  title = 'GSREMS READ API',
  version='1.0',
  doc='/docs',
  description="GSREMS READ TEST"
)


api.add_namespace(TestNamespace)