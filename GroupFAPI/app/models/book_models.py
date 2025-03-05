from app.extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    publication_date = db.Column(db.Date,nullable=False)
    isbn = db.Column(db.String(30), nullable=False, unique=True)
    genre = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=True)
   
 
    
    
    def __init__(self, id, title, pages, price, publication_date, isbn,genre, description,image):
        self.id = id
        self.title = title
        self.pages = pages
        self.price = price
        self.publication_date = publication_date
        self.isbn = isbn
        self.genre = genre
        self.description = description
        self.image = image
        
         
    def book_details(self, id, title, pages, price, publication_date, isbn, genre, description,image):
        return f"{self.id} {self.description} {self.publication_date} {self.isbn} {self.genre} {self.description} {self.image}"