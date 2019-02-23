from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, Searchbar
from timetable import valid_Account
from users import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oFmEakhRZdEjLpd0XTqg' #Secret key to encrypt session/cookie data should use Python os
                                                  #to generate a random 16 character key.


#Temp data for me to experiment with flask
posts = [
    {
        'author':'Bradley Harrison',
        'title':'First Post',
        'content':'This is my first post',
        'date_posted':'12/12/2018'
    }
]




@app.route("/home",methods=['GET','POST'])
def home():
    '''Home page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        search = Searchbar() #Creates the Searchbar Object containing the form
        return render_template('index.html',posts=posts,search=search) #Loads index.html - which is the homepage
    
    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in



@app.route("/" , methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    '''Login page for website'''
    
    form = LoginForm() #Creates login form object
    
    if 'username' in session: #Checks if the user is logged in and if they are then they get redirected
                              #to the home page.
        return redirect(url_for('home'))
    
    elif request.method == "POST": #Checks if the request method is POST
        if form.validate_on_submit() and valid_Account(form): #Checks if the forms have been filled in correctly
                                                              #need to give cases to show if it fails
            user = User(form.username.data) #Instanciate user object
                                                             
            if user.exists() and form.password.data == 'password': #Instead of if statement we should
                                                                                #be querying a database  
                session['username'] = user.fetch_User()  #Stores the user data in the session username - P.S. Need to findout why it
                                            #breaks when I use anything but username
                return redirect(url_for('home'))
            else:
                flash('Invalid Login Details!')
    return render_template('login.html',title='Login',form=form)


@app.route('/logout')
def logout():
    '''Closes the session and redirects the user to the login page'''
    session.pop('username',None) #Closes the users session
    return redirect(url_for('login'))



if __name__ == '__main__':
    app.run(debug=True)
    
    

