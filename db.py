from passlib.hash import pbkdf2_sha256

# test code
def skipTimetable(user,db):
	conn = sql.connect('harri361.mysql.pythonanywhere-services.com','harri361','RealWorldProject','harri361$VirtualCampus')
	c = conn.cursor()
	c.execute('''SELECT uid FROM users
		WHERE uid = ?''',(user,))
	user = c.fetchone()
	conn.close()
	if user:
		return True
	return False

print(skipTimetable('harri361'))

def new_User(uid,pwd,db):
	conn = sql.connect('harri361.mysql.pythonanywhere-services.com','harri361','RealWorldProject','harri361$VirtualCampus')
	c = conn.cursor()

	c.execute("INSERT INTO users(uid,pwd) VALUES (?,?)",(uid,pbkdf2_sha256.hash(pwd)))
	conn.commit()
	conn.close()
	return True

def validate_User(uid,pwd,db):
	conn = sql.connect('harri361.mysql.pythonanywhere-services.com','harri361','RealWorldProject','harri361$VirtualCampus')
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

