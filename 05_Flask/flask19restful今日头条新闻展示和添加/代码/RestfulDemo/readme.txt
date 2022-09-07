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


路由：
@app.route('/user')
def user():              -------》视图函数
    .....
    return response对象

增加  修改   删除   查询  按钮动作

http://127.0.0.1:5000/user?id=1
http://127.0.0.1:5000/user/1


restful: ---->api ----> 接口 ---->资源 ----> url

class xxx（Resource）：  -------> 类视图
    def get(self):
        pass
    ....

http://127.0.0.1:5000/user
get
post
put
delete
增加  修改   删除   查询  是通过请求方式完成的

路径产生:
api.add_resource(Resource的子类，'/user')
api.add_resource(Resource的子类，'/goods')
api.add_resource(Resource的子类，'/order')

endpoint:
http://127.0.0.1:5000/user/1

http://127.0.0.1:5000/goods?type=xxx&page=1&sorted=price   ----》get


----------------进：请求参数传入-------------------

步骤：
1。创建RequestParser对象：
# 参数解析
parser = reqparse.RequestParser(bundle_errors=True)  # 解析对象
2。给解析器添加参数：
    通过parser.add_argument('名字'，type=类型，required=是否必须填写，help=错误的提示信息，location=表明获取的位置form就是post表单提交)
    注意在type的位置可以添加一些正则的验证等。
    例如：
    parser.add_argument('username', type=str, required=True, help='必须输入用户名', location=['form'])
    parser.add_argument('password', type=inputs.regex(r'^\d{6,12}$'), required=True, help='必须输入6~12位数字密码',
                        location=['form'])
    parser.add_argument('phone', type=inputs.regex(r'^1[356789]\d{9}$'), location=['form'], help='手机号码格式错误')
    parser.add_argument('hobby', action='append')  # ['篮球', '游戏', '旅游']
    parser.add_argument('icon', type=FileStorage, location=['files'])
只要添加上面的内容，就可以控制客户端的提交，以及提交的格式。
3。在请求的函数中获取数据：
  可以在get，post，put等中获取数据，通过parser对象.parse_args()
  # 获取数据
  args = parser.parse_args()
  args是一个字典底层的结构中，因此我们获取具体的数据时可以通过get
  username = args.get('username')
  password = args.get('password')

------------输出-----------------


1.需要定义字典，字典的格式就是给客户端看的格式
user_fields = {
    'id': fields.Integer,
    'username': fields.String(default='匿名'),
    'pwd': fields.String(attribute='password'),
    'udatetime': fields.DateTime(dt_format='rfc822')
}

客户端能看到的是： id，username，pwd，udatetime这四个key
默认key的名字是跟model中的模型属性名一致，如果不想让前端看到命名，则可以修改
但是必须结合attribute='模型的字段名'

自定义fields
1。必须继承Raw
2。重写方法：
   def format(self):
        return 结果

class IsDelete(fields.Raw):
    def format(self, value):
        print('------------------>', value)
        return '删除' if value else '未删除'
user_fields = {
    。。。
    'isDelete1': IsDelete(attribute='isdelete'),
    。。。
}

URI:

xxxlist ----->点击具体的一个获取详情 ------> 详情

定义两个user_fields,
1.用于获取用户的列表信息结构的fields：
user_fields_1 = {
    'id': fields.Integer,
    'username': fields.String(default='匿名'),
    'uri': fields.Url('single_user', absolute=True)  ----》参数使用的就是endpoint的值
}

2。具体用户信息展示的fields
user_fields = {
    'id': fields.Integer,
    'username': fields.String(default='匿名'),
    'pwd': fields.String(attribute='password'),
    'isDelete': fields.Boolean(attribute='isdelete'),
    'isDelete1': IsDelete(attribute='isdelete'),
    'udatetime': fields.DateTime(dt_format='rfc822')
}

涉及endpoint的定义：

api.add_resource(UserSimpleResource, '/user/<int:id>', endpoint='single_user')


出：
return data
注意：data必须是符合json格式
{
  'aa':10,
  'bb':[
     {
       'id':1,
       'xxxs':[
                {},{}
              ]
     },
     {

     }
  ]
}
如果直接返回不能有自定义的对象User，Friend，。。。。

如果有这种对象，需要：marchal(),marchal_with()帮助进行转换。
1。marchal(对象，对象的fields格式)  # 对象的fields格式是指字典的输出格式
   marchal([对象，对象]，对象的fields格式)

2。marchal_with() 作为装饰器修饰请求方法

    @marshal_with(user_friend_fields)
    def get(self, id):
        。。。。
        return data

 函数需要参数，参数就是最终数据输出的格式

 参数： user_friend_fields，类型是：dict类型
 例如：
 user_friend_fields = {
    'username': fields.String,
    'nums': fields.Integer,
    'friends': fields.List(fields.Nested(user_fields))
}

fields.Nested(fields.String)  ----> ['aaa','bbb','bbbc']
fields.Nested(user_fields)  -----> user_fields是一个字典结构，将里面的每一个对象转成user_fields
-----》[user,user,user]


参考面试题：https://www.cnblogs.com/Utopia-Clint/p/10824238.html
