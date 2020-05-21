from flask import Flask
from flask_cors import CORS

def create_app(app_name='dog_memo'):
    app = Flask(app_name,
            static_folder = "./dist/static",
            template_folder = "./dist"
            )
    app.config.from_object('backend.config.BaseConfig')
    
    from backend.api import api
    app.register_blueprint(api, url_prefix="/api")
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app
