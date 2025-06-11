from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from .extension import db
from .config import Config

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    from .routes.auth_routes import auth_bp
    from .routes.product_routes import product_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/products')

    return app