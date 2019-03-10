import sqlite3



"""c.execute('''CREATE TABLE users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(10),
                first_name VARCHAR(20),
                last_name VARCHAR(20),
                course VARCHAR(40))''')

"""

"""c.execute('''INSERT INTO users (username,first_name,last_name,course) VALUES(
                "admin",
                "Administrative",
                "Account",
                "ADMIN")''')
conn.commit()"""


class User:
    def __init__(self, username):
        data = self.fetch_Data(username)
        self.__user_exists = False
        if data:
            self.__user_exists = True
            self.__user_name = data[1]
            self.__first_name = data[2]
            self.__last_name = data[3]
            self.__role = None
            self.__course = data[4]


    def fetch_Data(self, username):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users
                     WHERE username = ?''',(username,))
        
        return c.fetchone()
    
    def fetch_User(self):
        user = {}
        user['Username'] = self.__user_name
        user['Firstname'] = self.__first_name
        user['Lastname'] = self.__last_name
        user['Course'] = self.__course
        
        return user
    
    def exists(self):
        if self.__user_exists:
            return True
        else:
            return False
