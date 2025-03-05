from flask import Blueprint,request,jsonify


# company Blueprint
company = Blueprint('company', __name__,url_prefix='api/v1/company')

# company registration

@company.route('/register',methods=['POST'])  # Methods parameter is always a list
def register_company():
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({"ERROR":"All flelds are required"}),