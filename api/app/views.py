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
    user_name = sdata['user_name']
    password = sdata['password']
    confirm_password = sdata['confirm_password']
    newbie.signup(email, user_name, password, confirm_password)

    return jsonify(({'message': 'new user created'}), 201)

@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    if not request.json or not 'request_type' in request.json:
        abort(400)
    req = {
        'requestID': req_uest[-1]['requestID'] + 1,
        'request_type': request.json['request_type'],
        'clients_name': request.json.get('clients_name'),
        
    }
    req_uest.append(req)
    return jsonify( ({ 'Request': req_uest } ), 200)

@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return make_response(jsonify({'requests': dictionary}), 200)

@app.route('/api/v1/requests/<int:requestID>', methods=['PUT'])
def r_edit(requestID):
    req = {}
    req_data = request.get_json()
    for reqst in req_uest:
        if requestID == 0:
            abort (404)
        if requestID == reqst["requestID"]:
            req = reqst
            break

    req['request_type'] = req_data['request_type']

    return jsonify(req)
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
