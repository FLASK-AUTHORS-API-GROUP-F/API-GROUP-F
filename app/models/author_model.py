from app.models import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = 'author'
    author_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(23), nullable=False)
    last_name = db.Column(db.String(19), nullable=False)
    contact = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(27), nullable=False, unique=True)
    password = db.Column(db.String(17), nullable=False)
    image = db.Column(db.String(1), nullable=True)
    bio = db.Column(db.String(17), nullable=False)
    created_at = db.Column(db.DateTime,default = datetime.now())
    updated_at = db.Column(db.DateTime,onupdate = datetime.now())

    #the foreign keys
    book_id= db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    
    # here are the relationship to book
    books = db.relationship('Book', back_populates='author')
    
    
    def __init__(self,first_name,last_name,contact,email,password,image,bio,created_at,updated_at):
            self.first_name = first_name
            self.last_name = last_name
            self.contact = contact
            self.email = email
            self.password = password
            self.image = image
            self.bio = bio
            self.created_at = created_at
            self.updated_at = updated_at
        
    def author_details(self, author_id, first_name,  last_name, contact, email, password, image, bio, created_at,  updated_at):
        return f"{self.author_id} {self.first_name} {self.last_name} {self.contact} {self.email} {self.password} {self.image} {self.bio} {self.created_at} {self.updated_at}"
    
        
    
   