"""Flask Application
"""
from flask import Flask
from flask_cors import CORS
from apis.v1.views import app_views
from core.config.env import CONFIG


def create_app() -> Flask:
    """create application
    """
    _app = Flask(__name__)
    _app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    _app.register_blueprint(app_views, url_prefix='/api/v1')

    return _app


if __name__ == "__main__":
    app = create_app()
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    HOST = CONFIG['BENINPETRO_API_HOST']
    PORT = CONFIG['BENINPETRO_API_PORT']
    if not HOST:
        HOST = '0.0.0.0'
    if not PORT:
        PORT = '5000'
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
