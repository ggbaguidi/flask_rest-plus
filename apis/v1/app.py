"""Flask Application
"""
from os import environ
from flask import Flask
from flask_cors import CORS
from apis.v1.views import app_views


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


if __name__ == "__main__":
    HOST = environ.get('BENINPETRO_API_HOST')
    PORT = environ.get('BENINPETRO_API_PORT')
    if not HOST:
        HOST = '0.0.0.0'
    if not PORT:
        PORT = '5000'
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
