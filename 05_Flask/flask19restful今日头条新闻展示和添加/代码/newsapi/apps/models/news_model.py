from apps.models import BaseModel
from exts import db


class NewsType(BaseModel):
    __tablename__ = 'news_type'

    type_name = db.Column(db.String(50), nullable=False)
    newslist = db.relationship('News', backref='newstype')


class News(BaseModel):
    __tablename__ = 'news'

    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)
    news_type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='news')

    def __str__(self):
        return self.title


class Comment(BaseModel):
    __tablename__ = 'comment'

    content = db.Column(db.String(255), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))

    replys = db.relationship('Reply', backref='comment')

    def __str__(self):
        return self.content


class Reply(BaseModel):
    __tablename__ = 'reply'
    content = db.Column(db.String(255), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

    def __str__(self):
        return self.content
