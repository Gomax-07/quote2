from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


# Init app
app = Flask(__name__,instance_relative_config=True)

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

bootstrap.init_app(app)
db.init_app(app)

from app import views

app.run(debug=True)