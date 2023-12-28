from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker
import json
db = database()

#收藏模型
class Favorite(db.Base):
    __tablename__ = "favorites"
    #id
    id = Column(Integer, primary_key=True)
    #收藏夹id
    fid = Column(Integer)
    #用户名
    uid = Column(Integer)
    #视频id
    vid = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint([uid], ['users.id'], ondelete='CASCADE'),
        ForeignKeyConstraint([vid], ['videos.id'], ondelete='CASCADE'),
        ForeignKeyConstraint([fid], ['favorite_lists.id'], ondelete='CASCADE'),
    )
    #获取json
    def get_json(self):
        return {
            "id":self.id,
            "fid":self.fid,
            "uid":self.uid,
            "vid":self.vid
        }
        
    #获取jsonstr
    def get_jsonstr(self):
        return json.dumps(self.get_json())
db.create_tables()