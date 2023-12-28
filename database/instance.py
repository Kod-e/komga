from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Engine

class database:
    engine : Engine
    url : str = "mysql+pymysql://root:shrx9mhk@localhost/bdsm"
    Base = declarative_base()
    def __init__(self):
        self.engine = create_engine(self.url, echo=True)
    def create_tables(self):
        self.Base.metadata.create_all(self.engine)
    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session()