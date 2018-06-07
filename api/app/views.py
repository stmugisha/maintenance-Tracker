from flask import Flask, make_response, jsonify, request
from flask import flash, url_for, redirect, abort
from dbmodel.dbmodels import users
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

#instantiating app object
app = Flask(__name__)

newbie = users()

#Login_
@app.route('/api/v1/Login', methods=['GET', 'POST'])
def login():
    user = request.get_json()
    auth = request.authorisation
    if not auth or not auth(user['email']) or not auth(user['password']):
        return make_response('Missing login information', 401)
    
    if not user:
        return make_response(('Ghost user'),401)
    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'email':user['email'], 'exp': datetime.datetime.utcnow() + 
                            datetime.timedelta(minutes = 20)})
        
        return (jsonify({'Token': token.decode('UTF-8')}))
    return make_response(('Unable to verify submitted data.'), 401)  
    

#signup endpoint
@app.route('/api/v1/Signup', methods=['POST'])
def Signup():
    sdata = request.get_json()
    email = sdata['email']
    username = sdata['username']
    user_password = sdata['user_password']
    confirm_password = sdata['confirm_password']
    role = 'Normal user'
    if user_password != confirm_password:
        return jsonify(({'message': 'Unmatching passwords. Please try again.'}), 400)

    user_password = generate_password_hash(sdata['user_password'], method='sha256')
    confirm_password = generate_password_hash(sdata['confirm_password'], method='sha256')
    newbie.signup(email, username, user_password, confirm_password, role)
    return jsonify(({'message': 'new user created'}), 201)

#all users route
@app.route('/api/v1/users', methods = ['GET'])
def allUsers():
    return (jsonify(newbie.all_users()), 200)

#create request endpoint
@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    if not request.json or not 'request_type' in request.json:
        abort(400)

    req = request.get_json()    
    request_type = req['request_type']
    desscription = req['desscription']
        
    newbie.create_request(request_type, desscription)
    return jsonify(({ 'message': 'Your request has been successfully submitted' }), 200)

#get all requests endpoint
@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return(jsonify(newbie.get_all_requests()), 200)
    
#update request endpoint
@app.route('/api/v1/requests/<int:requestid>', methods=['PUT'])
def r_edit(requestid):
    redit = request.get_json()
    requestid = redit ['requestid']
    request_type = redit ['request_type']
    desscription = redit ['desscription']
    newbie.edit_request(request_type,desscription,requestid)
    if requestid < 0:
        return(jsonify({'message': 'invalid requestid'}), 404)
    return (jsonify({'message': 'Request successfully updated'}), 200)
#get request by id
@app.route('/api/v1/requests/<requestid>', methods=['POST'])
def get_requestID(requestid):
    return (jsonify(newbie.getby_id()), 200)


"""@app.route('/api/v1/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login')) 
"""
#starting the server
if __name__ == '__main__':
    app.run(debug=True)
