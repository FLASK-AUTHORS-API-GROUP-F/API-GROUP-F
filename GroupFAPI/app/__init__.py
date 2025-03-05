from flask import Flask
from app.extensions import db, migrate

# application factory function
def create_app():
    
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    #Registering models
    from app.models.author_models import Author
    from app.models.book_models import Book
    from app.models.company_models import Company
    
    
    
    # index route
    @app.route("/")
    def index():
        return "Hello"
    
    return app
