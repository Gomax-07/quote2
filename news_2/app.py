from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    reviews = db.relationship('Post', backref='author', lazy=True)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100),nullable=False)
  content = db.Column(db.Text,nullable=False)
  author = db.Column(db.String(25),nullable=False, default='Author unknown')
  date_posted = db.Column(db.DateTime,nullable=False,default= datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return  f"Review('{self.title}', '{self.date_posted}')"


reviews = [
  {
    'title':'review 1',
    'content':'content for app1',
    'author':'john'
  },
   {
    'title':'review 2',
    'content':'content for app2'
  }

]



@app.route('/home')
def index():
  return render_template("index.html")

@app.route('/news_article/')
def news_article():
  return render_template("news_article.html")

@app.route('/news_source/')
def news_source():
  return render_template("news_source.html")

@app.route('/reviews/')
def reviews():
  return render_template("reviews.html",reviews=reviews)

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





if __name__ == "__main__":
    app.run(debug=True)