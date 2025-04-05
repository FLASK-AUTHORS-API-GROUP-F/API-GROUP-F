from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db, migrate,jwt
from app.controllers.auth.auth_controller import auth

def create_app():  #application factory function
    
    app = Flask(__name__)#local variable
    app.config.from_object('config.Config')
    
    
    if __name__ == '__main__':
        app.run(debug=True)
        app.config["DEBUG"] = True


    db.init_app(app) #intializing app extension
    migrate.init_app(app, db)
    jwt.init_app(app)
    

    # importing and registering models 
    from app.models.author_model import Author
    from app.models.book_model import Book
    from app.models.company_model import Company
    from app.models.user import User
    
    #registering blueprints
    app.register_blueprint(auth)


    #index route to test the application
    @app.route('/') 
    def index():
        return "Welcome to my home page"
    return app
