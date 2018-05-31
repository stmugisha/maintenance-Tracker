from flask import Flask, make_response, jsonify, request
#instantiating app object
app = Flask(__name__)

credentials = [{'email':'msteve@admin.com','Password': 'admin'},
               {'email':'msteve@gmail.com', 'Password': 1234}]
req_uest = []
dictionary = {'Request Type':'car repair', 'Clients name':
              'steph', 'requestID': 1}

req_uest.append(dictionary)

#Login_form
@app.route('/api/v1/Login', methods=['GET', 'POST'])
def login():
    return 

@app.route('/api/v1/Signup', methods=['GET', 'POST'])
def Signup():
    return 

@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    new_rq = {'Request Type': request.json['Request Type'], 
            'Clients name': request.json['Clients name'], 
            'requestID': request.json['RequestID']}
    
    req_uest.append(new_rq)
    return jsonify({'request': req_uest})

@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return make_response(jsonify({'requests': req_uest}), 200)

@app.route('/myrequests/api/v1/<int:requestID>', methods=['PUT'])
def rID():
    

#starting the server
if __name__ == '__main__':
    app.run(debug=True)
