from flask import Flask, make_response, jsonify, request
from flask import flash, url_for, redirect, abort
from dbmodel.dbmodels import users
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

#instantiating app object
app = Flask(__name__)

app.config['SECRET KEY'] = 'thisissecret'

NewUser = users()

#Login_
@app.route('/Login', methods=['POST'])
def user_login():
    post_data = request.get_json()
    email = post_data ('email')
    user_password = post_data ('user_password')

    if not NewUser.login(email, user_password):
        return (jsonify({'message':'Invalid input data'})), 401
      
    token = jwt.encode({'email':email, 'exp' : datetime.datetime.utcnow() + 
                     datetime.timedelta(minutes = 20)}, app.config['SECRET KEY'])   
    return jsonify({'token': token.decode('UTF-8')}), 201
    
#signup endpoint
@app.route('/api/v1/Signup', methods=['POST'])
def Signup():

    signup_data = request.get_json()
    email = signup_data['email']
    username = signup_data['username']
    user_password = signup_data['user_password']
    confirm_password = signup_data['confirm_password']
    role = 'Normal user'
    
    if user_password != confirm_password:
        return jsonify (({'message': 'Unmatching passwords. Please try again.'}), 400)

    user_password = generate_password_hash(signup_data['user_password'], method='sha256')
    confirm_password = generate_password_hash(signup_data['confirm_password'], method='sha256')
    NewUser.signup(email, username, user_password, confirm_password, role)
    return jsonify(({'message': 'new user created'}), 201)

#all users route
@app.route('/api/v1/users', methods = ['GET'])
def allUsers():
    return (jsonify(NewUser.all_users()), 200)

#create request endpoint
@app.route('/api/v1/requests', methods = ['POST'])
def add_requests():
    if not request.json or not 'request_type' in request.json:
        abort(400)

    NewRequest = request.get_json()    
    request_type = NewRequest ['request_type']
    desscription = NewRequest ['desscription']
        
    NewUser.create_request(request_type, desscription)
    return jsonify(({ 'message': 'Your request has been successfully submitted' }), 200)

#get all requests endpoint
@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return(jsonify(NewUser.get_all_requests()), 200)
    
#update request endpoint
@app.route('/api/v1/requests/<int:requestid>', methods=['PUT'])
def r_edit(requestid):
    redit = request.get_json()
    requestid = redit ['requestid']
    request_type = redit ['request_type']
    desscription = redit ['desscription']
    NewUser.edit_request(request_type,desscription,requestid)
    if requestid < 0:
        return(jsonify({'message': 'invalid requestid'}), 405)
    return (jsonify({'message': 'Request successfully updated'}), 200)

#get request by id
@app.route('/api/v1/requests/<requestid>', methods=['POST'])
def get_requestID(requestid):
    return (jsonify(NewUser.getby_id()), 200)


"""@app.route('/api/v1/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login')) 
"""
#starting the server
if __name__ == '__main__':
    app.run(debug=True)
