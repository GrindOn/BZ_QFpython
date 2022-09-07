from flask import Flask

import settings
from apps.user.view import user_bp
from ext import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app)  # 将db对象与app进行了关联
    # 注册蓝图
    app.register_blueprint(user_bp)
    return app
