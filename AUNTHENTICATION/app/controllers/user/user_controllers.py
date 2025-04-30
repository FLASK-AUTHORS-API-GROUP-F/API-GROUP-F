from flask import Blueprint, request, jsonify
from app.status_code import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_201_CREATED
import validators
from app.models.user import User
from app.models.author_model import Author
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token

# User blueprint
user = Blueprint('Users', __name__, url_prefix='/api/v1/users')

# Getting all users from the database
@user.get('/')
@jwt_required()
def getAllUsers():
    try:
        all_users = User.query.all()
        users_data = []

        for user in all_users:
            user_info = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'user_name': user.user_name,
                'email': user.email,
                'contact': user.contact,
                'type': user.type,
                'created_at': user.created_at,
            }
            users_data.append(user_info)

        return jsonify({
            'Message': "Users retrieved successfully.",
            'total': len(users_data),
            'users': users_data
        }), HTTP_200_OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR


# Get all authors
@user.get('/authors')
@jwt_required()  # Protecting from unauthorized users
def getAllAuthors():
    try:
        all_authors = Author.query.filter_by(user_type='Author').all()
        authors_data = []

        for author in all_authors:
            author_info = {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'user_name': author.first_name,
                'email': author.email,
                'contact': author.contact,
                'biography': author.biography,
                'created_at': author.created_at,
                'companies': [],
                'books': []
            }

            if hasattr(author, 'books'):
                author_info['books'] = [
                    {'id': book.id, 'title': book.title, 'price': book.price,
                     'genre': book.genre, 'price_unit': book.price_unit,
                     'description': book.description, 'publication': book.publication,
                     'image': book.image, 'time_stamp': book.time_stamp}
                    for book in author.books
                ]

            if hasattr(author, 'companies'):
                author_info['companies'] = [
                    {'id': company.id, 'name': company.name, 'origin': company.origin}
                    for company in author.companies
                ]

            authors_data.append(author_info)

        return jsonify({
            'Message': "Authors retrieved successfully.",
            'total': len(authors_data),
            'authors': authors_data
        }), HTTP_200_OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR
