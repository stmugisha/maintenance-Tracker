from flask import Flask, make_response, jsonify, request
#instantiating app object
app = Flask(__name__)

credentials = [{'email':'msteve@admin.com','Password': 'admin'},
               {'email':'msteve@gmail.com', 'Password': 1234}]
req_uest = []
dictionary = {'Request_Type':'car repair', 'Clients name':
              'steph', 'requestID': 1}

req_uest.append(dictionary)

#Login_form
@app.route('/api/v1/Login', methods=['GET', 'POST'])
def login():
    return

@app.route('/api/v1/signup', methods=['GET', 'POST'])
def Signup():
    return 

@app.route('/api/v1/requests', methods=['POST'])
def add_requests():
    data=request.get_json()
    username=data['username']   
    return jsonify({'request': req_uest})

@app.route('/api/v1/requests', methods=['GET'])
def requests():
    return make_response(jsonify({'requests': dictionary}), 200)

@app.route('/api/v1/<string:Request_Type>', methods=['PUT'])
def r_edit(Request_Type):
    req_st = [requst for requst in req_uest if requst['Request_Type'] == Request_Type]
    req_st[0]['Request_Type'] = request.json['Request_Type']
    return jsonify({'Request_Type': req_st[0]})

#starting the server
if __name__ == '__main__':
    app.run(debug=True)
