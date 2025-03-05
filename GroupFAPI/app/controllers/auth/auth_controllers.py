from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_400_BAD_REQUEST,HTTP_500_INTERNAL_SERVER_ERROR
import validators
from app.models.author_models import Author
from app.extensions import db,bcrypt


# company Blueprint
auth = Blueprint('company', __name__,url_prefix='api/v1/auth')

# company registration

@auth.route('/register',methods=['POST'])  # Methods parameter is always a list
def register_company():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    contact = data.get('contact')
    email = data.get('email')
    type = data.get('type')
    password = data.get('password')
    bio = data.get('bio','') if type == 'author' else ''
    

# Validations of incoming request
    if not first_name or last_name or contact or email or type or password or bio :
        return jsonify({"ERROR":"All flelds are required"}),HTTP_400_BAD_REQUEST
    
    if type == 'author' and not bio:
        return jsonify({'ERROR':'Enter your author bio'}),HTTP_400_BAD_REQUEST
    
    if len(password) < 8:
        return jsonify({'ERROR':'Password is too short'}),HTTP_400_BAD_REQUEST
    
    if not validators.email(email):
        return jsonify({'ERROR':'Email is not valid'}),HTTP_400_BAD_REQUEST
    
    if Author.query.filter_by(email=email).first() is None:
        return jsonify({'ERROR':'Email address in use'}),HTTP_400_BAD_REQUEST
    
    
    # Creating a new author
    try:
        hashed_password = bcrypt.generate_password_hash(password) # Hashing the password
        new_author = Author(first_name=first_name,last_name=last_name,password=hashed_password,email=email,contact=contact)
        db.session.add(new_author)
        db.session.commit()
        
        
    # author name
       authorname = new_author. get_full_name()
    
        return jsonify({
            'message':authorname + "has been successfully created as an" + new_author.author_type,
            'author': {
                "id":new_author,
                "first_name":new_author.first_name,
                "last_name":new_author.last_name,
                 "contact":new_author.contact,
                 "email":new_author.email,
                 "type":new_author.author_type,
                 "password":new_author.password,
                 "bio":new_author.bio,
                 "crated_at":new_author.created_at
                 
            }
        }),
        
        
   
    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
        