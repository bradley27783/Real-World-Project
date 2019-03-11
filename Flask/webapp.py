from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import LoginForm, Searchbar
from timetable import valid_Account
from users import User
import difflib

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



@app.route("/home",methods=['GET','POST'])
def home():
    '''Home page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        searchB = Searchbar() #Creates the Searchbar Object containing the form
        query = submit(searchB)
        if(query!= 'None'):
            return searchWord()
        return render_template('index.html',posts=posts,search=searchB) #Loads index.html - which is the homepage
    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in


@app.route("/calendar",methods=['GET','POST'])
def calendar():
    '''Calender page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        searchB = Searchbar() #Creates the Searchbar Object containing the form
        query = submit(searchB)
        if(query!= 'None'):
            return searchWord()
        return render_template('calendar.html',posts=posts,search=searchB) #Loads calender.html - which is the calendar page
    
    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in
    
    
@app.route("/social",methods=['GET','POST'])
def social():
    '''Social page for website'''
    if 'username' in session:  #Checks if the user has a session if not then they can't access the homepage
        searchB = Searchbar() #Creates the Searchbar Object containing the form
        query = submit(searchB)
        if(query!= 'None'):
            return searchWord()
        return render_template('social.html',posts=posts,search=searchB) #Loads social.html - which is the social page
    
    else:
        return redirect(url_for('login')) #Redirect to display login page if user isn't logged in

    
@app.route("/group",methods=['GET','POST'])
def group():
    '''group page for website'''
    if 'username' in session:
        searchB = Searchbar()
        query = submit(searchB)
        if(query!= 'None'):
            return searchWord()
        return render_template('group.html',posts=posts,search=searchB) #Loads social.html - which is the social page
    
    else:
        return redirect(url_for('login'))
    
    
@app.route("/navigation",methods=['GET','POST'])
def navigation():
    '''Navigation page for website'''
    if 'username' in session:
        searchB = Searchbar()
        query = submit(searchB)
        if(query!= 'None'):
            return searchWord()
        return render_template('navigation.html',posts=posts,search=searchB)
    
    else:
        return redirect(url_for('login'))
    
    

def submit(search):
    '''Needs to return the correct search which will then be the x in redirect(url_for('bla bla bla))'''
    result = search.searchbar.data
    result = str(result)
    if(any(char.isdigit() for char in result)): #if has a number in -> room is being searched
        print("A Number is in result -> a room")
        return result
    else:
        print("No number is in result -> a building " + result)
        words = ["Alan Berry","Alma","Armstrong","Bugatti","Charles Ward","Engineering & Computing Building","ECG","ecg","Ellen Terry","George Eliot","Graham Sutherland","Frederick Lanchester Library","Jaguar","The Hub","Maurice Foss","James Starley","Multi-Storey Car Park","Priory Building","Richard Crossman","Alison Gingell Building","Sir John Laing","Sir William Lyons","Student Centre","Whitefriars","William Morris","Sport Centre"]
        results = difflib.get_close_matches(result, words)
        if(results!=[]):
            correctedResult = results[0]
            if(correctedResult == "ECG" or correctedResult =="ecg"):
                correctedResult = "Engineering & Computing Building"
            if(results!=correctedResult):
                print("Did you mean: ")
            return correctedResult
        if(result not in words):
            return "BadSearch"
        return result

    
@app.route('/search', methods=['GET','POST'])
def searchWord():
    '''Results of a search are shown here'''
    if 'username' in session:
        searchB = Searchbar()
        query = submit(searchB)
        if(query=="BadSearch"):
            value = "/static/images/campus_map.png"
            query = "No building found for your search"
            textValue = "Unfortunately, no buildings were found for your search"
            return render_template('search.html',value=value,value2=query,value3=textValue,posts=posts,search=searchB)
        elif(query!= 'None'):
            
            #QUEREY SENT HERE SHOULD BE ALREADY PREPARED INTO OUR SYSTEMS ACCEPTIBLE STRING
            
            #QUERY NOW HAS TO REPLACE EVRRY " " CHAR WITH "-"
            
            query2 = query.replace(' ', '-')
            value = "/static/images/" + query2 + ".png"
            
            
            #SHOULD QUERY MONGODB to get building desc here
            #gonna use text file temporarily

            readNextLine = False
            f = open("buildings.txt", "r")
            lines = f.readlines()
            textValue = "Gotta save the building description in the db - or tbh, probably wont be that bad here. Only 24, lets be honest"
            for l in lines:
                if readNextLine == True:
                    textValue = l
                    break
                if query in l:
                    readNextLine = True
            f.close()
            return render_template('search.html',value=value,value2=query,value3=textValue,posts=posts,search=searchB) #SENDS THE VARIABLE QUERY AS VALUE
    else:
        return redirect(url_for('login'))
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    

