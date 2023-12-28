from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKey,ForeignKeyConstraint,types,DateTime,VARCHAR
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
db = database()

#token模型
class Token(db.Base):
    __tablename__ = "tokens"
    #id
    uuid = Column(VARCHAR(36), primary_key=True,default=lambda: str(uuid4()))
    #用户名ID
    uid = Column(Integer)
    #设备名称
    device = Column(Text)
    #权限组
    permission = Column(Integer)
    #权限结束时间
    permission_end_time = Column(DateTime)
    __table_args__ = (
        ForeignKeyConstraint([uid], ['users.id'], ondelete='CASCADE'),
    )
    
db.create_tables()