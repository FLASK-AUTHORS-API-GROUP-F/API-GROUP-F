from app.extensions import db
from datetime import datetime

class Author(db.Model):
    __tablename__ = 'author'
    author_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(21), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    contact = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)
    image = db.Column(db.String(1), nullable=True)
    bio = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime,default = datetime.now())
    updated_at = db.Column(db.DateTime,onupdate = datetime.now())
    
    
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
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"
    def author_details(self, author_id, first_name,  last_name, contact, email, password, image, bio, created_at,  updated_at):
        return f"{self.author_id} {self.first_name} {self.last_name} {self.contact} {self.email} {self.password} {self.image} {self.bio} {self.created_at} {self.updated_at}"
    
        
    
   