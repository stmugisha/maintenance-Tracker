import psycopg2


class users:
    def __init__(self):
        self.connection = psycopg2.connect(database='Mtracker', user='postgres', host='localhost',
                                           password='12345', port='5432')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()   


    def login(self, email, password):
        pass

    def signup(self,email, username, user_password, confirm_password, role):
        self.cursor.execute("""INSERT INTO users (email,username, user_password,confirm_password,
                         role) VALUES(%s,%s,%s,%s,%s)""",(email,username,user_password,confirm_password,role))

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
        req_dict = {}
        for r in req:
            req_dict['requestid'] = r[0]
            req_dict['request_type'] = r[1]
            req_dict['desscription'] = r[2]
            
            all_requests.append(req_dict)
            req_dict = {}
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
        yrequest = self.cursor.fetchone()
        a_request = []
        areq_dict = {}
        for r in yrequest:
            areq_dict['requestid'] = r[0]
            areq_dict['request_type'] = r[1]
            areq_dict['desscription'] = r[2]
            
            a_request.append(areq_dict)
            areq_dict = {}
        return a_request
    