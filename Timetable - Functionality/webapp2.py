from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, Searchbar
#from timetable import valid_Account
from users import User
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, send
from timetableAPI import fetch_timetable, fetch_timetable3
from date import getCurrentDay

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oFmEakhRZdEjLpd0XTqg' #Secret key to encrypt session/cookie data should use Python os
                                                  #to generate a random 16 character key.
socketio = SocketIO(app)

displayTimes = ["09:00 - 10:00","10:00 - 11:00","11:00 - 12:00","12:00 - 13:00","13:00 - 14:00","14:00 - 15:00","15:00 - 16:00","16:00 - 17:00","17:00 - 18:00","18:00 - 19:00","19:00 - 20:00","20:00 - 21:00","21:00 - 22:00"]

times = {"09:00 - 10:00":"09:00","10:00 - 11:00":"10:00","11:00 - 12:00":"11:00","12:00 - 13:00":"12:00","13:00 - 14:00":"13:00","14:00 - 15:00":"14:00","15:00 - 16:00":"15:00","16:00 - 17:00":"16:00","17:00 - 18:00":"17:00","18:00 - 19:00":"18:00","19:00 - 20:00":"19:00","20:00 - 21:00":"20:00","21:00 - 22:00":"21:00"}
#Temp data for me to experiment with flask

@app.route("/event/<event>/<day>",methods=['GET','POST'])
def event(event,day):
    '''Calender page for website'''
    search = Searchbar() #Creates the Searchbar Object containing the form
    if day == 'today':
        day = getCurrentDay()
    return render_template('events1.html',search=search,event=event,day=day,displayTimes=displayTimes,times=times,timetable = fetch_timetable3(1),colour = "lightblue") #Loads calender.html - which is the calendar page


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    
    

