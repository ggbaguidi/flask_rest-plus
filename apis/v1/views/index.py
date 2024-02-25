""" Module of Index views
"""
from flask import jsonify
from flask_restx import Namespace, Resource


api = Namespace('index', description='Index of Index views')


@api.route('/', methods=['GET'], strict_slashes=False)
class Index(Resource):
    """Index class
    """
    @api.doc('get_status')
    def get(self) -> str:
        """ GET /api/v1/index
        Return:
            - the status of the API
        """
        return jsonify({"status": "OK"})
