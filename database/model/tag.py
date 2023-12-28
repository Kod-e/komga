from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker
import json
db = database()

#标签模型
class Tag(db.Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(Text,nullable=True)
    pic = Column(Text,nullable=True)
    #上级标签id
    parent_id = Column(Integer)
    __table_args__ = (
            ForeignKeyConstraint([parent_id], ['tags.id'], ondelete='CASCADE'),
    )
db.create_tables()