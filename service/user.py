from database.model import *
from service import *
from database.instance import database
from datetime import datetime, timedelta
db = database()

#单个User的服务
class UserService:
    session = db.get_session()
    #获取用户模型，isCreate为True时，表示注册，为False时，表示登录
    #失败返回False，成功返回True
    def __init__(self,id=None,name=None,password_md5=None,isCreate=False):
        #直接通过id获取用户
        if id:
            result = self.session.query(User).filter_by(id=id).first()
            if not result:
                raise Exception("no user")
            else:
                self.user = result
        #通过用户名和密码获取用户，但是不是注册
        elif name and password_md5 and not isCreate:
            result = self.session.query(User).filter_by(name=name,password_md5=password_md5).first()
            #如果用户不存在，返回False
            if not result:
                raise Exception("password error")
            else:
                self.user = result
        #通过用户名和密码获取用户，但是是注册
        elif name and password_md5 and isCreate:
            #通过用户名获取用户，如果用户存在，返回False
            result = self.session.query(User).filter_by(name=name).first()
            if result:
                raise Exception("same name")
            else:
                #创建用户
                self.user = self.create_user(name,password_md5)
    
    #创建用户
    def create_user(self,name,password_md5) -> User:
        new_user = User(
            name=name,
            password_md5=password_md5,
            premission=0,
            premission_end_time=datetime.now(),
            create_time=datetime.now()
        )
        self.session.add(new_user)
        self.session.commit()
        #创建收藏夹
        new_user = self.session.query(User).filter_by(name=name).first()
        favorite_list = FavoriteList(
            name='默认收藏夹',
            uid = self.user.id
        )
        self.session.add(favorite_list)
        self.session.commit()
        return new_user
    
    #创建token
    def create_token(self):
        token = Token(
            uid=self.user.id,
            device='default',
            permission=self.user.premission,
            permission_end_time = self.user.premission_end_time
        )
        self.session.add(token)
        self.session.commit()
        return token.uuid
    
    #升级用户组
    def upgrade_premission(self,premission,addtime):
        self.user.premission = premission
        #如果end_time小于当前时间，就直接加上addtime
        if self.user.premission_end_time < datetime.now():
            self.user.premission_end_time = datetime.now() + timedelta(days=addtime)
        else:
            self.user.premission_end_time = self.user.premission_end_time + timedelta(days=addtime)
        self.session.commit()
        return True
    
    #设置邮箱
    def set_email(self,email):
        self.user.email = email
        self.session.commit()
        return True

    #更改密码
    def change_password(self,password_md5):
        self.user.password_md5 = password_md5
        self.session.commit()
        return True
    
    #创建收藏夹
    def add_favorite_list(self,name) -> FavoriteListService:
        #创建时传递报错
        try:
            favorite_list = self.create_favorite_list(name)
        except Exception as e:
            raise e
        return favorite_list
    
    #获取收藏夹实例
    def delete_favorite_list(self,fid) -> FavoriteListService:
        #查询name和uid都符合的收藏夹
        favorite_list = FavoriteListService(self.user.id,fid=fid)
        return favorite_list
    
    #删除收藏
    def delete_favorite(self,vid):
        #查询收藏
        result = self.session.query(Favorite).filter_by(uid=self.user.id,vid=vid).first()
        if not result:
            raise Exception("no favorite")
        else:
            self.session.delete(result)
            self.session.commit()
    #获取所有收藏夹的数据库模型实例
    def get_favorite_lists(self):
        favorite_lists = self.session.query(FavoriteList).filter_by(uid=self.user.id).all()
        return favorite_lists
    
    #获取所有观看记录的数据库模型实例
    def get_histories(self):
        histories = self.session.query(History).filter_by(uid=self.user.id).all()
        return histories
    
    