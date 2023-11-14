from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'blahblah'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "database.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .dbmodels import User, Note, Flashcard

    if not os.path.exists(os.path.join(basedir, "database.db")):
      with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #tells flask where to redirect if not logged in
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(user_id): 
        return User.query.get(int(user_id)) #tells flask how load a user from database
        
  

    return app


