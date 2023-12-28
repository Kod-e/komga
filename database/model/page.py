from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint,Table
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
import json
db = database()

#页面模型
class Page(db.Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    #名称
    name = Column(Text,nullable=True)
    
    #获取json
    def get_json(self):
        return json.loads(self.json)
    #获取jsonstr
    def get_jsonstr(self):
        return self.get_json()
db.create_tables()