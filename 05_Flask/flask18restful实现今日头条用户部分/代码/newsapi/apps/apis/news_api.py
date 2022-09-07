from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from apps.models.news_model import NewsType

news_bp = Blueprint('news', __name__)
api = Api(news_bp)

types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}


class NewsTypeApi(Resource):
    @marshal_with(types_fields)
    def get(self):
        types = NewsType.query.all()
        return types  # NewsType属于自定义的一个类型


api.add_resource(NewsTypeApi, '/types')
