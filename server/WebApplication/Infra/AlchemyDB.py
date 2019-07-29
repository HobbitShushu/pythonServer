from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from application import dbconfig

engin_url = 'mysql+mysqlconnector://' + dbconfig['Setting']['user'] + ':' + \
            dbconfig['Setting']['password'] + '@' + \
            dbconfig['Setting']['host'] + '/' + \
            dbconfig['Setting']['database']
engine = create_engine(engin_url, convert_unicode=True)

# scoped_session - for thread safe
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))  
Base = declarative_base()

def init_db():
    metaData = MetaData()
    metaData.create_all(bind=engine)

class dbSession(object):
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()

class dbCommander(object):
    def __init__(self, model):
        self.model = model
       
    def to_list(self):
        entries = []
        # x - get table's column
        for q in self.model:
            entries.append({x.name: getattr(q, x.name) for x in q.__table__.columns})

        return entries
    
    def parsing(self):
        return {x.name: getattr(self.model, x.name) for x in self.model.__table__.columns}
