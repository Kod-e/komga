from database.model import *
from service import *
from database.instance import database
from datetime import datetime, timedelta
db = database()

#单个FavoriteList的服务
class FavoriteListService:
    session = db.get_session()
    def __init__(self,uid,isCreate=None,name=None,fid=None):
        #直接通过id获取用户
        if uid:
            result = self.session.query(User).filter_by(id=id).first()
            if not result:
                #如果用户不存在，抛出异常
                raise Exception("no user")
            else:
                self.user = result
                #如果是创建收藏夹，就创建收藏夹
                if isCreate and name:
                    #尝试创建收藏夹，如果收到异常就抛出异常
                    try:
                        self.favorite_list = self.create_favorite_list(name)
                    except Exception as e:
                        raise e
                    
                #如果不是创建收藏夹，就获取收藏夹
                elif fid:
                    result = self.session.query(FavoriteList).filter_by(id=fid).first()
                    if not result:
                        #如果收藏夹不存在，抛出异常
                        raise Exception("no favorite list")
                    else:
                        self.favorite_list = result
            
    #创建收藏夹
    def create_favorite_list(self,name) -> FavoriteList:
        #获取用户是否有同名收藏夹
        result = self.session.query(FavoriteList).filter_by(name=name,uid=self.user.id).first()
        if result:
            raise Exception("same name")
        #创建收藏夹
        new_favorite_list = FavoriteList(
            name=name,
            uid = self.user.id
        )
        self.session.add(new_favorite_list)
        self.session.commit()
        #query收藏夹，并返回
        new_favorite_list = self.session.query(FavoriteList).filter_by(name=name,uid=self.user.id).first()
        return new_favorite_list
    
    #获取收藏夹数据库模型的实例
    def get_model(self):
        return self.favorite_list
    
    #添加收藏
    def add_favorite(self,vid):
        #获取视频
        result = self.session.query(Video).filter_by(id=vid).first()
        if not result:
            raise Exception("no video")
        else:
            #创建收藏
            new_favorite = Favorite(
                uid = self.user.id,
                vid = vid,
                fid = self.favorite_list.id
            )
            self.session.add(new_favorite)
            self.session.commit()
    #删除收藏夹
    def delete_favorite_list(self):
        #删除收藏夹
        self.session.delete(self.favorite_list)
        self.session.commit()
