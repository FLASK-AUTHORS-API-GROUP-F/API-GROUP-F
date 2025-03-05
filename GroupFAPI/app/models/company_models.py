from app.extensions import db
from datetime import datetime

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(21), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    publication_date = db.Column(db.Date,nullable=False)
    created_at = db.Column(db.DateTime,default = datetime.now())
    updated_at = db.Column(db.DateTime,onupdate = datetime.now())
 
    
    
    def __init__(self, id, name, publication_date, description, created_at, updated_at):
        self.id = id
        self.name = name
        self.publication_date = publication_date
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
  
        
    def company_details(self, id, name, description,image, publication_date, created_at, updated_at):
        return f"{self.id} {self.name} {self.description} {self.publication_date} {self.created_at} {self.updated_at}"