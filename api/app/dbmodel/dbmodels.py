import psycopg2
               
class users:
    def __init__(self):
        self.connection = psycopg2.connect(database='Mtracker', user='postgres', host='localhost',
                                           password='12345', port='5432')
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()   
    
    def login(self, email, password):
         pass
    def signup(self,email, user_name, password, confirm_password):
        self.cursor.execute(("INSERT INTO users VALUES(%s,%s,%s,%s)"),(email,user_name,password,confirm_password))

    def all_users(self):
        self.cursor.execute("SELECT * FROM users")
 
    def create_request(self, request_type, desscription):
        new_request = "INSERT INTO requests VALUES(%s,%s)"
        self.cursor.execute(new_request)

    def get_all_requests(self):
        self.cursor.execute("SELECT * FROM requests")
