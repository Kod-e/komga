from database.instance import database
from sqlalchemy import create_engine, Column, Integer,String,Text,ForeignKeyConstraint,DateTime
from sqlalchemy.orm import sessionmaker

db = database()

#用户模型
class User(db.Base):
    __tablename__ = "users"
    #id
    id = Column(Integer, primary_key=True)
    #用户名
    name = Column(Text)
    #邮箱
    email = Column(Text,nullable=True)
    #md5密码
    password_md5 = Column(Text)
    #权限组
    premission = Column(Integer)
    #权限组结束时间
    premission_end_time = Column(DateTime)
    #注册时间
    create_time = Column(DateTime)
    
db.create_tables()