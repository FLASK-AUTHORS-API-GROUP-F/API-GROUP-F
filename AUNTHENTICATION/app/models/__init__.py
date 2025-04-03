

def create_app():
    #Importing and registering models
    from app.models.user import User
    from app.models.company_model import Company
    from app.models.book_model import Book


    #Registering blueprints
    app.register_blueprint(auth)

    @app.route("/")
    def home():
        return "Authors API Project setup"