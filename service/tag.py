from database.model import *
from service import *
from database.instance import database
from datetime import datetime, timedelta
db = database()

#单个Tag的服务
class TagService:
    session = db.get_session()
    #构造函数
    def __init__(self,id=None,isCreate=None,name=None,pic=None,parent_id=None):
        #直接通过id获取标签
        if id:
            result = self.session.query(Tag).filter_by(id=id).first()
            if not result:
                raise Exception("no tag")
            else:
                self.tag = result
        #创建标签
        elif isCreate and name and pic and parent_id:
            try:
                self.tag = self.create_tag(name,pic,parent_id)
            except Exception as e:
                raise e
            
    #创建标签
    def create_tag(self,name,pic,parent_id) -> Tag:
        #创建标签
        new_tag = Tag(
            name=name,
            pic=pic,
            parent_id=parent_id
        )
        self.session.add(new_tag)
        self.session.commit()
        #query标签，并返回
        new_tag = self.session.query(Tag).filter_by(name=name).first()
        return new_tag
    
    #删除标签
    def delete_tag(self):
        self.session.delete(self.tag)
        self.session.commit()
        
    #获取标签的子标签
    def get_children(self):
        result = self.session.query(Tag).filter_by(parent_id=self.tag.id).all()
        return result
    
    #获取所有拥有该标签的视频
    def get_videos(self):
        result = self.session.query(videoTag).filter_by(tag_id=self.tag.id).all()
        return result
    
    