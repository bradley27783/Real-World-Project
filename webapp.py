from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, Searchbar, AccountForm, DeleteForm
from timetable import getTimetable
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16) #Secret key to encrypt session/cookie data should use Python os
                                                  #to generate a random 16 character key.

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="harri361",
    password="RealWorldProject",
    hostname="harri361.mysql.pythonanywhere-services.com",
    databasename="harri361$VirtualCampus"
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#campus information table
class Campus(db.Model):
    campus_name = db.Column(db.String(50), primary_key=True)
    city = db.Column(db.String(10), nullable = False)
    building = db.relationship('Building',backref='campus',lazy='select')

#building information
class Building(db.Model):
    building_name = db.Column(db.String(30), primary_key=True)
    campus_name = db.Column(db.String(50),db.ForeignKey('campus.campus_name'))
    rooms = db.relationship('Room',backref='building',lazy=True)

#rooms timetable
class Room(db.Model):
    room_number = db.Column(db.String(5), primary_key=True)
    room_type = db.Column(db.String(10), primary_key=True)
    building_name = db.Column(db.String(30),db.ForeignKey('building.building_name'),nullable=False)
    timetable = db.relationship('Timetable',backref='room',lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    fname = db.Column(db.String(20),nullable=False)
    lname = db.Column(db.String(20),nullable=False)
    course = db.Column(db.String(40),nullable=False)
    timetable_fetched = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    timetable = db.relationship('Timetable',backref='user',lazy=True)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.password}',{self.fname})"

#timetalbe database
class Timetable(db.Model):
    start_time = db.Column(db.DateTime, primary_key=True)
    end_time = db.Column(db.DateTime, primary_key=True)
    day = db.Column(db.String(10), primary_key=True)
    module_name = db.Column(db.String(30),unique=True,nullable=False)
    room_number = db.Column(db.String(5),db.ForeignKey('room.room_number'),nullable=False)
    lecturer_name = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

"""
#events information table
class events_info(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_location = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable = False)
    event_time = db.Column(db.DateTime, nullable = False)
    #course_relevant = db.Column(db.String(30), nullable=False, default='everyone')
"""
"""
#chat information
class chat_log(db.Model):
    log_id = db.Column(db.Integer(10), primary_key=True)
    sender_id = db.Column(db.Integer(7), nullable = False)
    receiver_id = db.Column(db.Integer(10), nullable = False)
    message = db.Column() #need data type
    time_stamp = db.Column(db.DateTime(7), nullable = False)

#group table
class group_table(db.Model):
    group_log_id = db.Column(db.Integer(10), primary_key=True)
    group_name = db.Column(db.Varchar(10), nullable = False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.password}',{self.fname})"

"""

#Temp data for me to experiment with flask
posts = [
    {
        'author':'Bradley Harrison',
        'title':'First Post',
        'content':'This is my first post',
        'date_posted':'12/12/2018'
    }
]
URI = "https://webapp.coventry.ac.uk/Timetable-main/"

@app.route("/" , methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    '''Login page for website'''
    form = LoginForm() #Creates login form object


    if 'username' in session: #Checks if the user is logged in and if they are then they get redirected
                                  #to the home page.
        return redirect(url_for('home'))

    elif request.method == "POST": #Checks if the request method is POST
        user = request.form['username']
        pwd = request.form['password']

        try:
            db_user = User.query.filter_by(username=user).first()
            print(db_user)
            if db_user and pbkdf2_sha256.verify(pwd, db_user.password):
                if db_user.fname == "default" or db_user.lname == "default" or db_user.course == "null":
                    session['temp'] = user
                    return redirect(url_for('setup'))


                elif form.validate_on_submit() and db_user.username == 'admin':
                    print("[DEBUG] Test 1")
                    session['username'] = user
                    session['name'] = db_user.fname
                    print("[DEBUG] Admin Login")
                    return redirect(url_for('home'))

                elif form.validate_on_submit(): #Checks if the forms have been filled in correctly
                    session['username'] = user
                    session['name'] = db_user.fname
                    print("[DEBUG] passed check 1122")
                    return redirect(url_for('home'))
                        #need to give cases to show if it fails
                        #user = User(form.username.data) #Instanciate user object

                        #if user.exists() and form.password.data == 'password': #Instead of if statement we should
                                                                                            #be querying a database
                            #session['username'] = user.fetch_User()  #Stores the user data in the session username - P.S. Need to findout why it
                                                        #breaks when I use anything but username

            elif form.validate_on_submit():
                if getTimetable(user, pwd, URI):
                    print("Logging in...")
                    db.session.add(User(username=user,password=pbkdf2_sha256.hash(pwd),fname="default",lname="default",course="null"))
                    db.session.commit()
                    session['temp'] = user
                    return redirect(url_for('setup'))

                else:
                    flash("Incorrect Details Provided! The Details Provided Above Are Either Incorrect Or You Are Not A CU Student! Please Check Details And Try Again", 'danger')
                    return redirect(url_for("login"))

            else:
                print("[DEBUG] FAILED")

                if not db_user or not pbkdf2_sha256.verify(pwd, db_user.password):
                    print("[DEBUG] Incorrect Details")
                    flash("Incorrect Details Provided! The Details Provided Above Are Either Incorrect Or You Are Not A CU Student! Please Check Details And Try Again", 'danger')
                    return redirect(url_for("login"))

        except AttributeError as e:
            print("[ERROR] ValueError")

            if e.args[0] == "'NoneType' object has no attribute 'password'":
                print("[DEBUG] FAILED 2")

                if not db_user or not pbkdf2_sha256.verify(pwd, db_user.password):
                    print("[DEBUG] Incorrect Details 2")
                    flash("Incorrect Details Provided! The Details Provided Above Are Either Incorrect Or You Are Not A CU Student! Please Check Details And Try Again", 'danger')
                    return redirect(url_for("login"))

        except ValueError as e:
            print("[ERROR] ValueError")

            if e.args[0] == 'not a valid pbkdf2_sha256 hash':
                print("[ERROR] Incorrect password")
                #flash(f"")
            print(e.args)
        except Exception as e:
            print(type(e))
            print(e.args)

    return render_template('login.html',title='Login',form=form)


@app.route('/setup', methods=['GET','POST'])
def setup():
    '''Login page for website'''
    account = AccountForm() #Creates account form object

    if 'username' in session: #Checks if the user is logged in and if they are then they get redirected
                              #to the home page.
        return redirect(url_for('home'))

    elif 'temp' not in session:
        return redirect(url_for('login'))

    elif request.method == "GET": #If the page is being called load this template
        return render_template('accountsetup.html',title='First Time Setup',account=account)

    elif request.method == "POST": #Checks if the request method is POST
        fname = request.form['fname']
        lname = request.form['lname']
        course = request.form['course']

        if account.validate_on_submit():

            db_user = User.query.filter_by(username=session['temp']).first()
            db_user.fname = fname
            db_user.lname = lname
            db_user.course = course
            db.session.commit()


            session['username'] = session['temp']
            session['name'] = fname
            session.pop('temp',None)
            return redirect(url_for('home'))

    return render_template('accountsetup.html',title='First Time Setup',account=account)


@app.route('/account', methods=['GET','POST'])
def account():
    '''Login page for website'''

    delete = DeleteForm()
    print("1")
    if 'username' in session: #Checks if the user is logged in and if they are then they get redirected
                              #to the home page.
        search = Searchbar()
        print("2")
        if request.method == "GET": #If the page is being called load this template
            return render_template('account.html',title='Account Settings',search=search, delete=delete)

        elif request.method == "POST": #Checks if the request method is POST
            print("3")
            pwd = request.form['password']
            user = User.query.filter_by(username=session['username'])
            user_data = User.query.filter_by(username=session['username']).first()
            if delete.validate_on_submit():
                print("4")
                print(user)
                print(pwd)
                if pbkdf2_sha256.verify(pwd, user_data.password):
                    print("5")
                    user.delete()
                    db.session.commit()

                    return redirect(url_for('logout'))
                else:
                    print("6")
                    flash("Incorrect Password!", 'danger')
                    return redirect(url_for("account"))

    elif 'temp' not in session:
        return redirect(url_for('login'))

    return render_template('account.html',title='Account Settings',search=search, delete=delete)


@app.route('/logout')
def logout():
    '''Closes the session and redirects the user to the login page'''
    session.pop('username',None) #Closes the users session
    session.pop('name',None)
    return redirect(url_for('login'))



@app.route("/home",methods=['GET','POST'])
def home():
    '''Home page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        search = Searchbar() #Creates the Searchbar Object containing the form
        return render_template('index.html',posts=posts,search=search) #Loads index.html - which is the homepage

    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in


@app.route("/event/<event>",methods=['GET','POST'])
def event(event):
    '''Calender page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        search = Searchbar() #Creates the Searchbar Object containing the form
        return render_template('events.html',posts=posts,search=search,event=event) #Loads calender.html - which is the calendar page

    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in

@app.route("/social",methods=['GET','POST'])
def social():
    '''Social page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        search = Searchbar() #Creates the Searchbar Object containing the form
        return render_template('social.html',posts=posts,search=search) #Loads social.html - which is the social page

    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in


@app.route("/group/<d_group>",methods=['GET','POST'])
def group(d_group):
    '''group page for website'''
    print("\n\n" + d_group + "\n\n")
    session['group'] = d_group
    print(session)
    print(request.path)
    if 'username' in session:
        search = Searchbar()
        return render_template('group.html',posts=posts,search=search, group=d_group)

    else:
        return redirect(url_for('login'))


@app.route("/navigation",methods=['GET','POST'])
def navigation():
    '''Navigation page for website'''
    if 'username' in session:
        search = Searchbar()
        return render_template('navigation.html',posts=posts,search=search)

    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()


