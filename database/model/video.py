from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker

db = database()

#视频模型
class Video(db.Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    #名称
    name = Column(Text)
    
    #播放url
    play = Column(Text) #h264默认
    hevc_play = Column(Text,nullable=True) #hevc
    
    #图片url
    picture = Column(Text) #jpg默认
    webp_picture = Column(Text,nullable=True) #webp
    avif_picture = Column(Text,nullable=True) #avif
    
    #视频标签
    subtitle = Column(Text)
    #描述
    description = Column(Text)

db.create_tables()