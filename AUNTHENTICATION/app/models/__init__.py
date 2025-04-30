from flask import Flask
from app.extensions import db, bcrypt, jwt, migrate
# from app.routes.auth import auth  # Import your authentication blueprint
from app.models.user import User
from app.models.company_model import Company
from app.models.book_model import Book

def create_app():
    app = Flask(__name__)

    # App configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/database_name"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "your_secret_key"

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth)

    @app.route("/")
    def home():
        return "Authors API Project setup"

    return app
