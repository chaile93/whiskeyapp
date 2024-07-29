#THIS MAKES THE WEBSITE FOLDER A PYTHON PACKAGE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


#THIS IS HOW WE WILL IMPORT AND CREATE OR DATABASE TO STORE INFO
db = SQLAlchemy()
DB_NAME = "whiskey.db"


#DEFINE OUR APP NAME WITH A KEY
def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY'] = 'i need a drink'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.ffeahodvdatbkywcmcvu:164748Cajh!@aws-0-us-east-1.pooler.supabase.com:6543/postgres" #THIS SAYS WHERE MY SQL DATABASE IS LOCATED 
    db.init_app(app)#THIS TELLS IT THAT THIS DATABASE WILL BE USED WITH THIS APP
    
    
    #IMPORT OUR URL ROUTES BLUEPRINTS TO OUR PAGES 
    from .views import views 
    from .auth import auth
    
    #REGISTER THE BLUEPRINT ROUTES, YOU NEED THIS IN ORDER TO GET IT TO SHOW ON SERVER GIRL!! 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    

    return app

def create_database(app): #this checks if a database already exists and if not it will create it
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)#this tells which app we are creating the database for 
        print('Created Database!')
        
        
        
