from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db, migrate,jwt

def create_app():  #application factory function
    
    app = Flask(__name__)#local variable
    app.config.from_object('config.Config')
    

    db.init_app(app) #intializing app extension
    migrate.init_app(app, db)
    jwt.init_app(app)
    

    #registering models 
    from app.models.author_model import Author
    from app.models.book_model import Book
    from app.models.company_model import Company
    from app.models.user import User
    
    #index route to test the application
    @app.route('/') 
    def index():
        return "World"
    return app
