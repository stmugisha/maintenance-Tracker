from flask import Flask, make_response, jsonify, request
from flask import flash, url_for, redirect, abort
from flask_login import login_user, logout_user
from validate_email import validate_email
#instantiating app object
app = Flask(__name__)

users = [{'email':'steve@admin.com','password': 'admin'},
               {'email':'steve@gmail.com', 'Password': 1234}]
req_uest = []
dictionary = {'request_type':'car repair', 'clients_name':
              'steph', 'requestID': 1}

req_uest.append(dictionary)

#Login_
@app.route('/api/v1/Login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    if not email or not password:
        return make_response(jsonify({'message': 'all fields are required'}), 400)

        valid_email = validate_email('email')
        if not valid_email:
            return make_response(jsonify({'message': 'invalid email address'}), 400)

        for user in users:
            if user[email] == email and user[password] == password:
                return make_response(jsonify({'message': 'You are logged in'}), 200)

        make_response(jsonify({'message': 'Invalid username or password.'}), 400)
    make_response(jsonify({'Please login'}), 400)

@app.route('/api/v1/Signup', methods=['POST'])
def Signup():
    sdata = request.get_json()
    email = sdata['email']
    password = sdata['password']
    confirm_password = sdata['confirm_password']
    users.append(sdata)

    return jsonify({'message': 'new user created'})

@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    if not request.json or not 'request_type' in request.json:
        abort(400)
    req = {
        'requestID': req_uest[-1]['requestID'] + 1,
        'request_type': request.json['request_type'],
        'clients_name': request.json.get('clients_name'),
        'done': False
    }
    req_uest.append(req)
    return jsonify( ({ 'Request': req_uest } ), 200)

@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return make_response(jsonify({'requests': dictionary}), 200)

@app.route('/api/v1/<string:request_type>', methods=['PUT'])
def r_edit(request_type):
    #req_st = [reqst for reqst in req_uest if reqst['request_type'] == request_type]
    inst = request.get_json()
    req_uest=  inst.get("request_type")
    if req_uest:
        abort(400)
    else:
        return jsonify({'request_type': req_uest})

@app.route('/api/v1/<string:requestID>', methods=['GET'])
def get_requestID(re):
    pass


@app.route('/api/v1/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login'))
#starting the server
if __name__ == '__main__':
    app.run(debug=True)
