from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, Searchbar
from timetable import valid_Account

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oFmEakhRZdEjLpd0XTqg'


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
@app.route("/home",methods=['GET','POST'])
def home():
    '''Home page for website'''
    search = Searchbar()
    return render_template('index.html',posts=posts,search=search)

@app.route('/login', methods=['GET','POST'])
def login():
    '''Login page for website'''
    form = LoginForm()
    if form.validate_on_submit() and valid_Account(form):
        if form.username.data == 'admin' and form.password.data == 'admin':
            return redirect(url_for('home'))
        else:
            flash('Invalid Login Details!')
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)
