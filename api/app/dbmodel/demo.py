from dbmodels import users

usr = users()
print(usr.get_all_requests())
"""@app.route('/api/v1/requests/<int:requestID>', methods=['PUT'])
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

    return jsonify(req)"""