"""My api for the Project
"""
from flask import Blueprint
from flask_restx import Api
from apis.v1.views.index import api as index

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

api = Api(
    app=app_views,
    title="My api",
    version='1.0'
)

api.add_namespace(index)
