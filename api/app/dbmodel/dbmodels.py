import psycopg2
               
class users:
    def __init__(self):
        self.connection = psycopg2.connect(database='Mtracker', user='postgres', host='localhost',
                                           password='12345', port='5432')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()   
    
    def login(self, email, password):
         pass
    def signup(self,email, username, pwd, confirm_password, role):
        self.cursor.execute("""INSERT INTO users (email,username, user_password,confirm_password,
                         role) VALUES(%s,%s,%s,%s,%s)""",(email,username,pwd,confirm_password,role))

    def all_users(self):
        self.cursor.execute("SELECT * FROM users")
        
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
        