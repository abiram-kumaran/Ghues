from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, makedirs
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "project.db"

def create_database(app):
    # Ensure instance directory exists
    if not path.exists(app.instance_path):
        makedirs(app.instance_path, exist_ok=True)
    
    db_path = path.join(app.instance_path, DB_NAME)
    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("Created database!")

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # Use relative path since instance_relative_config=True
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SECRET_KEY"] = "your_secret_key"  # Required for session management and CSRF protection
    db.init_app(app)

    # Import models
    from . import models
    from .models import User, Post, Comment, Like

    # Create the database
    create_database(app)

    # Register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Initialize Login Manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
