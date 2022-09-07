from apps.models import BaseModel
from exts import db


class NewsType(BaseModel):
    __tablename__ = 'news_type'

    type_name = db.Column(db.String(50), nullable=False)


class News(BaseModel):
    __tablename__ = 'news'

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    news_type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
