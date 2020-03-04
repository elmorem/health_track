import os
from flask import Flask
from flask_sqlalchemy import flask_SQLAlchemy


basedir=os.path.abspath(os.path.dirname(__file__))



app.config['SQLALCHEMY_DATABASE_URI'] = postgresql://mark:elmorem@localhost/ht_db

