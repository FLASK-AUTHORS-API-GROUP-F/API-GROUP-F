from app.extensions import db
from datetime import datetime

class Book(db.Model):

    
    __tablename__ = "books"  # Naming convention for table
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    no_of_pages = db.Column(db.Integer, nullable=False)
    price = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    isbn = db.Column(db.String(30), nullable=True, unique=True)
    # company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))  # assuming you have a companies table
    image = db.Column(db.String(255), nullable=True)
    # company = db.relationship('Company', backref='books')  # Correctly reference the 'Company' model
    # author = db.relationship('User', backref='books')  # Correctly reference the 'User' model
    publication_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, no_of_pages, price, description, genre, isbn, image=None):
        self.title = title
        self.no_of_pages = no_of_pages
        self.price = price
        self.description = description
        self.genre = genre
        self.isbn = isbn
        # self.company = company
        # self.author = author
        self.image = image
