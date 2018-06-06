from flask import Flask, make_response, jsonify, request
from flask import flash, url_for, redirect, abort
from dbmodel.dbmodels import users
#from validate_email import validate_email
#instantiating app object
app = Flask(__name__)

user = [{'email':'steve@admin.com','password': 'admin'},
               {'email':'steve@gmail.com', 'Password': 1234}]
req_uest = []
dictionary = {'request_type':'car repair', 'clients_name':
              'steph', 'requestID': 1}

req_uest.append(dictionary)

newbie = users()

#Login_
@app.route('/api/v1/Login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    pass


@app.route('/api/v1/Signup', methods=['POST'])
def Signup():
    sdata = request.get_json()
    email = sdata['email']
    username = sdata['username']
    user_password = sdata['user_password']
    confirm_password = sdata['confirm_password']
    role = sdata['role']
    newbie.signup(email, username, user_password, confirm_password, role)

    return jsonify(({'message': 'new user created'}), 201)

@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    if not request.json or not 'request_type' in request.json:
        abort(400)

    req = request.get_json()    
    request_type = req['request_type']
    desscription = req['desscription']
        
    newbie.create_request(request_type, desscription)
    return jsonify(({ 'message': 'Your request has been successfully submitted' }), 200)

@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return(jsonify(newbie.get_all_requests()), 200)
    

@app.route('/api/v1/requests/<int:requestID>', methods=['PUT'])
def r_edit(requestID):
    
    return jsonify()
@app.route('/api/v1/<string:requestID>', methods=['GET'])
def get_requestID(requestID):
    pass


"""@app.route('/api/v1/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login')) 
"""
#starting the server
if __name__ == '__main__':
    app.run(debug=True)
