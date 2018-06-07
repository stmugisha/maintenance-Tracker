import psycopg2
from flask import request

class users:
    def __init__(self):
        self.connection = psycopg2.connect(database='Mtracker', user='postgres', host='localhost',
                                           password='12345', port='5432')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()   


    def login(self, email, user_password):
        self.cursor.execute("SELECT email, user_password FROM users WHERE email = '{}' AND user_password = '{}'".format(email, user_password))
                            
        active = self.cursor.fetchall()
        current_users = []
        user_dict = {}

        for user in active:
            user_dict ['userid'] = user [0]
            user_dict ['email'] = user [1]
            user_dict ['username'] = user [2]
            user_dict ['user_password'] = user [3]

            current_users.append(user_dict)
            user_dict = {}
        return current_users

    def signup(self, email, username, user_password, confirm_password, role):
        self.cursor.execute("""INSERT INTO users (email,username, user_password,
                            confirm_password,  role) VALUES(%s,%s,%s,%s,%s)""",
                            (email, username, user_password, confirm_password, role))

    def all_users(self):
        self.cursor.execute("SELECT * FROM users")
        user = self.cursor.fetchall()
        all_user = []
        user_dict = {}
        for u in user:
            user_dict['userid'] = u[0]
            user_dict['email'] = u[1]
            user_dict['username'] = u[2]
            user_dict['user_password'] = u[3]
            user_dict['confirm_password'] = u[4]
            user_dict['role'] = u[5]
            
            all_user.append(user_dict)
            user_dict = {}
        return all_user

    def create_request(self, request_type, desscription):
        self.cursor.execute("""INSERT INTO requests(request_type,desscription) VALUES(%s,%s)""", 
                           (request_type,desscription))

    def get_all_requests(self):
        self.cursor.execute("SELECT * FROM requests")
        req = self.cursor.fetchall()
        all_requests = []
        ResquestDictionary = {}
        for row in req:
            ResquestDictionary ['requestid'] = row [0]
            ResquestDictionary ['request_type'] = row [1]
            ResquestDictionary ['desscription'] = row [2]
            
            all_requests.append(ResquestDictionary)
            ResquestDictionary = {}
        return all_requests

    def edit_request(self,requestid,request_type,desscription):
        edit = """UPDATE requests
                SET request_type = %s,
                    desscription = %s
                WHERE requestid = %s;
                """
        self.cursor.execute(edit,(requestid,request_type,desscription))

    def getby_id(self):
        self.cursor.execute( """SELECT * 
                    FROM requests
                    WHERE requestid = requestid;
                   """)
        RequestById = self.cursor.fetchone()
        a_request = []
        request_dictionary = {}
        for Request in RequestById:
            request_dictionary['requestid'] = Request [0]
            request_dictionary['request_type'] = Request [1]
            request_dictionary ['desscription'] = Request [2]
            
            a_request.append(request_dictionary)
            request_dictionary = {}
        return a_request
    