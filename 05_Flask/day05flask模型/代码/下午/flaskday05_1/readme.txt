1.模板
网页 ----》模板引擎处理 ----〉模板
        render_template
{{ 变量 }}

{% if 条件 %}  {%endif%}
for,block,macro,with

{% extends '' %}
{% include '' %}
{% import '' %}
{% set username = '' %}

过滤器：
。。。
自定义过滤器
    1。通过方法添加
    2。装饰器

2. 蓝图
from flask import Blueprint, url_for

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def user_center():
    print(url_for('user.register'))  # 反向解析
    return '用户中心'


@user_bp.route('/register')
def register():
    return '用户注册'

今天的内容：

1。flask-script
pip install flask-script

使用里面的Manager进行命令得到管理和使用：
manager = Manager(app=app)

manager.run()  ---->启动

使用命令在终端：
python3 app.py runserver    ---->Runs the Flask development server

python3 app.py runserver -h 0.0.0.0 -p 5001

自定义添加命令：
@manager.command
def init():
    print('初始化')

python3 app.py init

2. 搭建数据库：
mtv：
model  模型  ----》数据库
template 模板
view  视图

安装：
pip3 install pymysql        建公路

pip3 install flask-sqlalchemy    实现ORM映射

pip3 install flask-migrate     发布命令工具


步骤：
1。配置数据库的连接路径
# mysql+pymysql://user:password@hostip:port/databasename
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskday05'

2。flask-sqlalchemy的搭建：
创建包ext
   __init__.py中添加：

   db = SQLAlchemy()   ---->必须跟app联系

   def create_app():
        ....
        db.init_app(app)

        return app
3. flask-migrate的配置：
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


4.创建模型：
  models.py

  模型就是类，经常称作模型类

  class User(db.Model):      ------> user表
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)

  常见的数据类型：
  Integer        整型
  String(size)   字符串类型，务必指定大小
   Text          长文本类型
  DateTime       日期时间
   Float         浮点类型
  Boolean        布尔类型
  PickleType     存储pickle类型  主要跟序列化有关
  LargeBinary    存储大的二进制类型

 可选的：
  primary_key=True   主键
  autoincrement=True  自增
  nullable=False      不允许为空
  unique=True         唯一
  default=datetime.now  默认值  可以设置成当前系统时间或者其他的值


5.使用命令：
    a. ************敲黑板***************
       在app.py 中导入模型:from apps.user.models import User

    b. 在终端使用命令：db
        python3 app.py db init   -----》 产生一个文件夹migrations
        python3 app.py db migrate -----> 自动产生了一个版本文件
         项目
          | ---apps
          | ---ext
          | ---migrations    python3 app.py db init     只需要init一次
                   |---versions   版本文件夹
                        |---71edde7ee937_.py    ---》  python3 app.py db migrate  迁移
                        |---cc0dca61130f_.py
                                                      python3 app.py db upgrade 同步
                                                      python3 app.py db downgrade 降级

6.添加数据：以注册为例：
# 模板，视图与模型结合

# 1. 找到模型类并创建对象
user = User()
# 2. 给对象的属性赋值
user.username = username
user.password = password
user.phone = phone
# 添加
# 3.将user对象添加到session中（类似缓存）
db.session.add(user)
# 4.提交数据
db.session.commit()







