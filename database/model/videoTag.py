from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker

db = database()

#视频标签模型
class VideoTag(db.Base):
    __tablename__ = "video_tags"
    id = Column(Integer, primary_key=True)
    vid = Column(Integer)
    tid = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint([vid], ['videos.id'], ondelete='CASCADE'),
        ForeignKeyConstraint([tid], ['tags.id'], ondelete='CASCADE'),
    )

db.create_tables()