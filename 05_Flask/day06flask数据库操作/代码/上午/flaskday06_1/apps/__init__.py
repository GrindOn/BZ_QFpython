from flask import Flask

from apps.user.view import user_bp
from exts import db
from settings import DevelopmentConfig


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)
    # 初始化db
    db.init_app(app=app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    # print(app.url_map)
    return app
