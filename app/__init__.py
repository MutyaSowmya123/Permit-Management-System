from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    from app.routes import auth, permit, admin
    app.register_blueprint(auth.bp)
    app.register_blueprint(permit.bp)
    app.register_blueprint(admin.bp)

    @app.route('/')
    def home():
        return render_template('home.html')  # This will render templates/home.html

    return app
