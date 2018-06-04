import unittest
from app import app
import json
class TestClass(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_requests(self):
        response = {'Request_Type':'car repair', 'Clients name':
              'steph', 'requestID': 1}
        
        my_request = self.tester.get('api/v1/requests', content_type = 'application/json')
        request_resp = json.loads(my_request.data.decode())
        self.assertEqual(response, request_resp["requests"])

    #check that users can add requests
    def test_create_requests(self):
            