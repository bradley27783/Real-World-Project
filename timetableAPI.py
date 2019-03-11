import sqlite3

def fetch_timetable(username):
    conn = sqlite3.connect('timetableDB.db')
    cur = conn.cursor()
    timetable = cur.execute('''SELECT * FROM StudentTimetable
                            WHERE username = ?;''',(username,))
    
    return timetable.fetchone()    

