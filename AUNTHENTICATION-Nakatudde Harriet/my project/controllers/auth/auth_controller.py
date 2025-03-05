from flask import Blueprint, request,jsonify
from app.status_code import HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED 
import validators
from app.models.user import User
from app.extensions import db, Bcrypt

auth = Blueprint('auth', __name__,url_prefix='api/v1/auth')

#user registration

@auth.route('/register',methods=['POST'])
def register_user():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    contact = data.get('contact')
    email = data.get('email')
    user_type = data.get('user_type')
    password = data.get('password')
    biograpy = data.get('biograpy','') if type =="author"else ''

    if not first_name or not last_name or not contact or not email:
        return jsonify({"error":"All fields are required"}),HTTP_400_BAD_REQUEST
    
    if type == "author" and not biograpy:
        return jsonify({"error":"Enter your author biograpy"}),HTTP_400_BAD_REQUEST
    
    if len(password) <8 :
        return jsonify({"error":"Password is too short"}),HTTP_400_BAD_REQUEST
    
    if not validators.email(email):
        return jsonify({"error":"Email is not valid"}),HTTP_201_CREATED
    
    if Author.query.filter_by(email=email).first() is not None:
        return jsonify({"error":"Email is not valid"}),HTTP_201_CREATED
    
    try:
        hashed_password = bcrypt.generate_password_hash('hunter2')#hashing the password

        #creating the user
        new_user = User(first_name = first_name,last_name=last_name,password=hashed_password,email=email, 
                        contact=contact,biograpy=biograpy,user_type=user_type)
        db.session.add(new_user)
        db.session.commit()

        #username
        username = new_user. get_full_name()
        return jsonify({
            'message': username + "has been successfully created as an" + new_user.user_type,
            'user':{
                "id":new_user.id,
                "firstname":new_user.first_name,
                "lasttname":new_user.last_name,
                "email":new_user.email,
                "contact":new_user.contact,
                "biograpy":new_user.biography,
                "created_at":new_user.created_at,

            }
        }),HTTP_201_CREATED 



    except Exception as :
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR 
    


    


