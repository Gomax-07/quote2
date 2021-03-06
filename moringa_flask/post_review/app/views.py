from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from app import app

app = Flask(__name__)
app.config['SECRET_KEY'] = '4da30bd01c4cd12344b9a7d1b4fb7784'

reviews = [
    {
        'author': 'John james',
        'title': 'Blog Review ',
        'content': 'First review content',
        'date_posted': 'June 11,2020'
    },
    {
        'author': 'Amy Joy',
        'title': 'Blog Review 2',
        'content': 'A review  content',
        'date_posted': 'May 29, 2020'
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('index.html', reviews=reviews)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
  app.run(debug=True)