import unittest
from app.views import app
import json
from flask_login import current_user
from app.dbmodel.dbmodels import users

class TestClass(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
    #get all requests check
    def test_requests(self):
        response = {'request_type':'car repair', 'desscription':'faulty engine'}
        
        my_request = self.tester.get('api/v1/requests', content_type = 'application/json')
        request_resp = json.dumps(my_request.data.decode())
        self.assertEqual(response, request_resp['all_requests'])

    #checking that users can add requests
    def test_add_req(self):
        dta = {'request_type':'phone repair', 'desscription':
              'cracked screen'}
        response = self.tester.post('/api/v1/requests', content_type = 'application/json', 
                                     data = json.dumps(dta))

        self.assertEqual(response.status_code, 200)

    #check that incorrect request is not posted.
    def test_incorrect_req(self):
        response = self.tester.post('/api/v1/requests')
        self.assertEqual(response.status_code, 400)

    #check invalid request modification.
    def test_edit_req(self):
        response = self.tester.put('/api/v1/requests/<int:requestid>', content_type = 'application/json',)
        self.assertEqual(response.status_code, 404)

