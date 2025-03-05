from app.extensions import db

from datetime import datetime

class Company(db.Model):

    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())
    

    def __init__(self,id, name, email, image, bio, password, contact , location):
          self.id = id 
          self.name = name
          self.email = email
          self.image = image
          self.bio = bio
          self.password = password
          self.email = email
          self.contact = contact
          self.location = location


     
    def __repr__(self):
        return f"<Company {self.name}>"
   



        



