from database.instance import database
from sqlalchemy import create_engine, Column, Integer,Text,ForeignKey,ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker

db = database()

#列表展示方式
class ViewList(db.Base):
    __tablename__ = "viewlists"
    #id
    id = Column(Integer, primary_key=True)
    #列表名称
    name = Column(Text,nullable=True)
    #列表类型
    type = Column(Integer)
    #列表排序
    order = Column(Integer)
    #pageid
    pid = Column(Integer)
    #tid
    tid = Column(Integer)
    __table_args__ = (
        ForeignKeyConstraint([pid], ['pagess.id'], ondelete='CASCADE'),
        ForeignKeyConstraint([tid], ['tags.id'], ondelete='CASCADE'),
    )
db.create_tables()