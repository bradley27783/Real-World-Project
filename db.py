import sqlite3
from passlib.hash import pbkdf2_sha256


def create_Table():
        conn = sqlite3.connect('vc.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY, uid VARCHAR(20), pwd TEXT, fname VARCHAR(20))''')

        # Insert a row of data
        c.execute("INSERT INTO users(uid,pwd,fname) VALUES (?,?,?)",("admin",pbkdf2_sha256.hash('admin'),'Administrator'))
        conn.commit()
        conn.close()

def display():
        conn = sqlite3.connect('vc.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM users''')
        print(c.fetchall())
        conn.close()

#create_Table()
#display()

# test code
def skipTimetable(user):
	conn = sqlite3.connect('vc.db')
	c = conn.cursor()
	c.execute('''SELECT uid FROM users
		WHERE uid = ?''',(user,))
	user = c.fetchone()
	conn.close()
	if user:
		return True
	return False

print(skipTimetable('harri361'))

def new_User(uid,pwd):
	conn = sqlite3.connect('vc.db')
	c = conn.cursor()

	c.execute("INSERT INTO users(uid,pwd) VALUES (?,?)",(uid,pbkdf2_sha256.hash(pwd)))
	conn.commit()
	conn.close()
	return True

def validate_User(uid,pwd):
	conn = sqlite3.connect('vc.db')
	c = conn.cursor()

	c.execute("""SELECT pwd FROM users
		WHERE uid = ?""",(uid,))

	user = c.fetchone()
	conn.close()

	print(user)

	if user and pbkdf2_sha256.verify(pwd, user[0]):
		print("[DEBUG] CORRECT PASSWORD")
		return True

	else:
		print("[DEBUG] INCORRECT PASSWORD")
		return False


