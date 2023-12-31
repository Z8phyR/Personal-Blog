from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'site.db')


db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

login_manager = LoginManager(app)
# Specifies the name of the view to redirect to when a user needs to log in.
login_manager.login_view = 'login'

from myblog import routes, models

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
