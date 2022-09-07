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