#this project uses flask-login,Flask-SQLAlchemy and flask , os, remember for the requirements txt! 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__) #this references the module that we are going to use to run this app
    app.config['SECRET_KEY'] = "habadolad"
    return app



