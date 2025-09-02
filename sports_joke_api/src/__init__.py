from flask import Flask
from src.routes import sports_joke_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(sports_joke_bp, url_prefix='/')
    return app