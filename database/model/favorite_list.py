from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker
import json

db = database()

#收藏模型
class FavoriteList(db.Base):
    __tablename__ = "favorite_lists"
    #id
    id = Column(Integer, primary_key=True)
    #收藏夹名称
    name = Column(Text,nullable=True)
    #用户名
    uid = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint([uid], ['users.id'], ondelete='CASCADE'),
    )
    #获取json
    def get_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "uid":self.uid
        }
        
    #获取jsonstr
    def get_jsonstr(self):
        return json.dumps(self.get_json())
db.create_tables()