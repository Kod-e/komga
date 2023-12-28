from database.model import *
from service import *
from database.instance import database
from datetime import datetime, timedelta
db = database()

#单个Video的服务
class VideoService:
    session = db.get_session()
    
    #通过id创建VideoService
    def __init__(self,id=None,isCreate=None,name=None,play=None,picture=None,subtitle=None,description=None):
        
        #直接通过id获取视频
        if id:
            result = self.session.query(Video).filter_by(id=id).first()
            if not result:
                raise Exception("no video")
            else:
                self.video = result
        #创建视频
        elif isCreate and name and play and picture and subtitle and description:
            try:
                self.video = self.create_video(name,play,picture,subtitle,description)
            except Exception as e:
                raise e
            
    #创建视频
    def create_video(self,name,play,picture,subtitle,description) -> Video:
        #创建视频
        new_video = Video(
            name=name,
            play=play,
            picture=picture,
            subtitle=subtitle,
            description=description
        )
        self.session.add(new_video)
        self.session.commit()
        #query视频，并返回
        new_video = self.session.query(Video).filter_by(name=name).first()
        return new_video
    
    #删除视频
    def delete_video(self):
        #删除视频
        self.session.delete(self.video)
        self.session.commit()
        
    #观看视频
    def watch_video(self,token) -> str:
        #查找token
        result = self.session.query(Token).filter_by(token=token).first()
        #如果token不存在，抛出异常
        if not result:
            raise Exception("no token")
        #如果token的permission不是1，抛出异常
        elif result.permission != 1:
            raise Exception("no premission")
        else:
            #创建观看记录
            new_history = History(
                uid=result.uid,
                vid=self.video.id,
                watch_time=datetime.now()
            )
        self.session.commit()
        #返回视频的播放地址
        return self.video.play
    
    #获取视频的标签
    def get_tags(self):
        result = self.session.query(videoTag).filter_by(vid=self.video.id).all()
        return result
    
    #删除视频的某个标签
    def delete_tag(self,tid):
        result = self.session.query(videoTag).filter_by(vid=self.video.id,tid=tid).all()
        for i in result:
            self.session.delete(i)
        self.session.commit()
        
    #给视频添加标签
    def add_tag(self,tid):
        #查找标签
        result = self.session.query(Tag).filter_by(id=tid).first()
        #如果标签不存在，抛出异常
        if not result:
            raise Exception("no tag")
        else:
            #创建标签
            new_tag = videoTag(
                vid=self.video.id,
                tid=tid
            )
            self.session.add(new_tag)
            self.session.commit()
            
    