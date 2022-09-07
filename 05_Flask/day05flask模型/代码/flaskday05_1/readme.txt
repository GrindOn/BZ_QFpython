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

2。 蓝图


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

2. 数据库：
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

2。创建包ext
   __init__.py中添加：

   db = SQLAlchemy()   ---->必须跟app联系

   def create_app():
        ....
        db.init_app(app)

        return app
3. migrate:








