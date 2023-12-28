from database.instance import database
from sqlalchemy import create_engine, Column, Integer,Text,ForeignKeyConstraint,VARCHAR,DateTime
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
db = database()

#订单模型
class Trade(db.Base):
    __tablename__ = "trades"
    #id
    uuid = Column(VARCHAR(36), primary_key=True,default=lambda: str(uuid4()))
    #用户名ID
    uid = Column(Integer)
    #时间(天)
    time = Column(Integer)
    #金额
    money = Column(Integer)
    #支付方式
    trade_method = Column(Text)
    #订单状态
    trade_status = Column(Integer)
    #订单来源
    trade_from = Column(Text)
    #支付时间
    trade_time = Column(DateTime)
    #订单活动
    trade_active = Column(Integer)
    
    __table_args__ = (
        ForeignKeyConstraint([uid], ['users.id'], ondelete='CASCADE'),
    )
db.create_tables()