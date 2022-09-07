1. 路由
192.168.1.10:8080
@app.route('/index')
def index():
    return ''

URL : http://192.168.1.10:8080/index

route:
    def route(self, rule, **options):
        def decorator(f):
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
这个装饰器其实就是将rule字符串跟视图函数进行了绑定，通过add_url_rule()实现的绑定
@app.route('/index')
def index():
    return 'welcome everyone！'

等效的
def index():
    return 'welcome everyone！'
app.add_url_rule('/index', view_func=index)


2.路由的变量规则：

string  （缺省值） 接受任何不包含斜杠的文本   *
int      接受正整数  *
float    接受正浮点数
path     类似 string ，但可以包含斜杠
uuid     接受 UUID 字符串


@app.route('/getcity/<key>')  # key就是一个变量名，默认是字符串类型的
def get_city(key):  # 参数是必须添加的
    print(type(key))
    return data.get(key)

2. 视图
返回值：其实返回值返回的都是一个响应对象。
response响应对象

print(response.content_type)
print(response.headers)
print(response.status_code)  # 200
print(response.status)  # 200 OK

request请求对象：只需要导入，通过from flask import request
导入之后可以获取对象的属性和方法
属性：
    print(request.headers)  # request对象 对象访问属性，也可以调用方法
    print(request.path)
    print(request.full_path)
    print(request.base_url)
    print(request.url)
跟请求方法相关的：
    get：
    request.args 底层是字典的形式   主要获取get提交的请求参数
    如果是get请求格式是这个样子的：/register2?username=zhangsan&address=Beijing
    此时的username是form表单中表单元素的name值
    print(request.args.get('username'))   # 获取值
    print(request.args.get('address'))

    post:
    request.form 底层是字典的形式   主要获取post提交的请求参数
    注意post提交必须在路由中进行设置，通过methods = ['GET','POST']
    按照此种形式：
    @app.route('/register2', methods=['GET', 'POST'])
    def register2():  # 获取页面提交的内容
        .......  内容省略
    获取数据：
    print(request.form)  # 如果请求方法是post则需要通过request.form取值
    print(request.form.get('username'))
    print(request.form.get('address'))

3.模板

如果想在视图函数中获取模板xxx.html的内容则通过render_template()
render_template('模板名称') 返回值是一个字符串
主要是通过模板引擎将模板内容转成字符串的形式。
@app.route('/register')
def register():
    return render_template('register.html')
