from app.extensions import db
from datetime import datetime

class User(db.Model):

    
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.String(50), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Text(200), nullable=False)
    biography = db.Column(db.Text(200), nullable=True)  # Corrected typo
    user_type = db.Column(db.String(20), default='Author')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    def __init__(self, first_name, last_name, email, contact, image, password, biography, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.image = image
        self.password = password
        self.biography = biography
        self.user_type = user_type


    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"