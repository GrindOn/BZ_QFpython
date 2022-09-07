一、跨域问题来源于JavaScript的"同源策略"，即只有 协议+主机名+端口号 (如存在)相同，
则允许相互访问。也就是说JavaScript只能访问和操作自己域下的资源，
不能访问和操作其他域下的资源。跨域问题是针对JS和ajax的，html本身没有跨域问题。
后端：
1。使用第三方扩展
flask-cors

from flask_cors import CORS
cors= CORS()

与app进行绑定
cors.init_app(app=app,supports_credentials=True)

2。response = make_response()
response.headers['Access-Control-Allow-Origin']='*'
response.headers['Access-Control-Allow-Methods']='GET,POST'
response.headers['Access-Control-Allow-Headers']='x-request-with,Content-type'
return response

二、蓝图与api使用：
user_bp = Blueprint('user', __name__)

api = Api(user_bp)

class xxxxApi(Resource):
    pass

api.add_resource(xxxxApi,'/xxxx')


三、
在OAuth协议中，token是在输入了用户名和密码之后获取的，
利用这个token你可以拥有查看或者操作相应的资源的权限。
你有这些权限，是因为服务器知道你是谁（authentication）以后赋予你的，
所以token这个东西，其实就是你的一个“代表”，或者说完全能代表你的“通行证”。
从这个概念来说，“令牌”这个翻译，真的是非常的“信雅达”啊


