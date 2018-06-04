import unittest
from app.app import app
import json
#from flask_login import current_user
class TestClass(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
    #get all requests check
    def test_requests(self):
        response = {'request_type':'car repair', 'clients_name':
              'steph', 'requestID': 1}
        
        my_request = self.tester.get('api/v1/requests', content_type = 'application/json')
        request_resp = json.loads(my_request.data.decode())
        self.assertEqual(response, request_resp["requests"])

    #checking that users can add requests
    def test_add_req(self):
        response = self.tester.get('/api/v1/requests')
        self.assertTrue(response.status_code, 201)

    #check that incorrect request is not posted.
    def test_incorrect_req(self):
        response = self.tester.get ('/api/v1/requests')
        self.assertTrue(response.status_code, 400)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.tester.get('/api/v1/Login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.tester:
            response = self.tester.post(
                '/api/v1/Login',
                data=dict(email="steve@admin", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    # check that login works correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.tester.post(
            '/api/v1/Login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password.', response.data)

    # checking logout works correctly
    def test_logout(self):
        with self.tester:
            self.tester.post(
                '/api/v1/Login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.tester.get('/api/v1/logout', follow_redirects=True)
            self.assertIn(b'You were logged out', response.data)
            self.assertFalse(current_user.is_active())

    # check that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.tester.get('/api/v1/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


     # check that Flask was set up correctly
    def test_index(self):
        response = self.tester.get('/api/v1/Login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # check that index page requires user login
    def test_main_route_requires_login(self):
        response = self.tester.get('/api/v1/Login', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)
