from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm
from timetable import valid_Account

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oFmEakhRZdEjLpd0XTqg'

posts = [
    {
        'author':'Bradley Harrison',
        'title':'First Post',
        'content':'This is my first post',
        'date_posted':'12/12/2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html',posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit() and valid_Account(form):
        if form.username.data == 'admin' and form.password.data == 'admin':
            return redirect(url_for('home'))
        else:
            flash('Invalid Login Details!')
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)
