from database.model import *
from service import *
from database.instance import database
from datetime import datetime, timedelta
db = database()

#单个Page的服务
class PageService:
    session = db.get_session()
    
    #构造函数
    def __init__(self,id=None,isCreate=None,name=None):
        #直接通过id获取页面
        if id:
            result = self.session.query(Page).filter_by(id=id).first()
            if not result:
                raise Exception("no page")
            else:
                self.page = result
        #创建页面
        elif isCreate and name:
            try:
                self.page = self.create_page(name)
            except Exception as e:
                raise e
            
    #创建页面
    def create_page(self,name) -> Page:
        #创建页面
        new_page = Page(
            name=name
        )
        self.session.add(new_page)
        self.session.commit()
        #query页面，并返回
        new_page = self.session.query(Page).filter_by(name=name).first()
        return new_page
    
    #删除页面
    def delete_page(self):
        self.session.delete(self.page)
        self.session.commit()
        
    #添加viewlist
    def add_viewlist(self,name:str,type:int,order:int,tid:int):
        #获取标签
        result = self.session.query(Tag).filter_by(id=tid).first()
        if not result:
            raise Exception("no tag")
        else:
            #创建viewlist
            new_viewlist = ViewList(
                name=name,
                type=type,
                order=order,
                tid=tid,
                pid=self.page.id
            )
            self.session.add(new_viewlist)
            self.session.commit()
            
    #删除viewlist
    def delete_viewlist(self,vid):
        #获取viewlist
        result = self.session.query(ViewList).filter_by(id=vid).first()
        if not result:
            raise Exception("no viewlist")
        else:
            #删除viewlist
            self.session.delete(result)
            self.session.commit()
            
    #获取viewlist,返回数据库模型实例,按照order排序
    def get_viewlists(self):
        result = self.session.query(ViewList).filter_by(pid=self.page.id).order_by(ViewList.order).all()
        return result