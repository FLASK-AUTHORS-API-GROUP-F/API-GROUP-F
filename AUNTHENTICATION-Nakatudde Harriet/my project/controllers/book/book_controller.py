from flask import Blueprint, request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
import validators
from app.models.book_model import Company
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity, create_refresh_token




#company blueprint
book = Blueprint('book', _name_, url_prefix='/api/v1/book')

#creating companies

@book.route('/create', methods=['POST'])
@jwt_required(get_jwt_identity)
def createBook():
    data = request.json
    origin= data.get('origin')
    description = data.get('description')
    user_id = data.get('user_id')
    name = data.get('name')
    


    #validations of the incoming request

    if not name or not origin or not description:
        return jsonify({"error":"All fields are required"}),HTTP_400_BAD_REQUEST
    

    if Book.query.filter_by(name=name).first() is not None:
        return jsonify({"error":"Company name already exists."}),HTTP_409_CONFLICT
    
    
    try:
      

       #creating a new company
       new_book = Book(name=name,origin = origin, description=description, user_id=user_id)
       db.session.add(new_book)
       db.session.commit()



       return jsonify({
           'message': name + " has been successfully created as an " + new_book.user_type,
           'user':{
               'id':new_book.id,
               "name":new_book.name,
               "origin":new_book.origin,
               "description": new_book.description
              
           }
       }),HTTP_201_CREATED

    except Exception as e:   
        db.session.rollback() 
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    book_controllers