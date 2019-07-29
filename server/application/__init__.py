from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
#application.config['SECRET_KEY'] = 'dlsfhr0309!'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dlsfhr0309!@localhost/data'
#application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(application)

app = application
#app.debug = True

buff_size = 128

import json
with open('./application/dbconfig.json') as data_file:
    dbconfig = json.load(data_file)

from WebApplication.Infra.AlchemyDB import init_db
init_db()

from WebApplication.Infra.Cache import RedisController
cache = RedisController(**dbconfig['Redis_DB'])

from application import Route

from WebApplication.Document.Models import User

