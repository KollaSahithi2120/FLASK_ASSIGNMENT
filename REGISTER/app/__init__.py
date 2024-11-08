from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize app with extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Ensure 'main.login' matches your route

    # Import blueprints and models after initializing app components
    with app.app_context():
        from app.routes import main  # Import the blueprint
        app.register_blueprint(main)  # Register the blueprint
        
        from app.models import User  # Import models

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.models import User  # Import User model here to avoid circular import
    return User.query.get(int(user_id))
