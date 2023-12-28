from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKeyConstraint,DateTime
from sqlalchemy.orm import sessionmaker
import json
db = database()

#访问记录模型
class History(db.Base):
    __tablename__ = "video_logs"
    id = Column(Integer, primary_key=True)
    #用户id
    uid = Column(Integer)
    #视频id
    vid = Column(Integer)
    #访问时间
    time = Column(DateTime)
    __table_args__ = (
        ForeignKeyConstraint([vid], ['videos.id'], ondelete='CASCADE'),
    )
    #获取json
    def get_json(self):
        return {
            "id":self.id,
            "uid":self.uid,
            "vid":self.vid,
            "time":self.time
        }
    #获取jsonstr
    def get_jsonstr(self):
        return json.dumps(self.get_json())
db.create_tables()