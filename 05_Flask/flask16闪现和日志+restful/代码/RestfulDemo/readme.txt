什么是RESTful架构：

（1）每一个URI代表一种资源；

（2）客户端和服务器之间，传递这种资源的某种表现层；

（3）客户端通过四个HTTP动词(GET,POST,PUT,DELETE,[PATCH])，对服务器端资源进行操作，实现"表现层状态转化"。

Postman

前后端分离：
前端： app，小程序，pc页面

后端： 没有页面，mtv： 模型模板视图  去掉了t模板。
      mv：模型 视图
      模型的使用：跟原来的用法相同
      视图： api构建视图
  步骤：
     1. pip3 install flask-restful

     2.创建api对象
      api = Api(app=app)
      api = Api(app=蓝图对象)
     3.
      定义类视图：
      from flask_restful import Resource
      class xxxApi(Resource):
        def get(self):
            pass

        def post(self):
            pass

        def put(self):
            pass

        def delete(self):
            pass
      4. 绑定

      api.add_resource(xxxApi,'/user')

参照：http://www.pythondoc.com/Flask-RESTful/quickstart.html
https://flask-restful.readthedocs.io/en/latest/

出：


进：