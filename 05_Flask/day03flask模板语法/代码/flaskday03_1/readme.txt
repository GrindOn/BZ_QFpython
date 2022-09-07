1. 路由
@app.route('/')
def test():
    pass

变量规则：
str，int ,float, path ,uuid

import uuid

uid = uuid.uuid4()
格式

2. 视图函数：

 返回值：
      类型： 字符串，dict，tuple，response, WSGI

      response对象  响应对象

      response('字符串',headers={key:value})

      response = make_response('.....')

      response.headers['aaa'] = 'abc'

        print(response.content_type)
        print(response.headers)
        print(response.status_code)  # 200
        print(response.status)  # 200 OK



      request对象
      from flask import request

      request.path
      request.full_path
      ....

      重点：
      request.args   --->get请求  http://127.0.0.1:5000/register?username=zhangsan&password=123456
      request.form   --->post请求

视图函数的返回值：
response响应：
1。str     自动转成response对象
2。dict    json
3。response对象  response对象
4。make_response()  response对象
5。redirect()   重定向  302状态码
6。render_template()  模板渲染 + 模板


模板：（网页）
模板的语法：
1. 在模板中获取view中传递的变量值：{{ 变量名key }}

render_template('模板名字',key=value,key=value)

    name = '沈凯'  # str
    age = 18  # int
    friends = ['建义', '陈璟', '小岳岳', '郭麒麟']  # list
    dict1 = {'gift': '大手镯', 'gift1': '鲜花', 'gift2': '费列罗'}  # dict
    # 创建对象
    girlfriend = Girl('美美', '安徽阜阳')  # 自定义的类构建的类型：Girl对象

模板：
    {{ list.0 }}  同 {{ list[0] }}
    {{ dict.key }} 同 {{ dict.get(key) }}
    {{ girl.name }} 同 {{ 对象.属性 }}

 2.  控制快:
 {% if  条件 %}

 {% endif %}

 {% if  条件 %}
     条件为True
 {% else %}
     条件为False
 {% endif %}


 {% for 变量 in 可迭代的对象 %}
    for循环要做的任务

 {% endfor %}

可以使用loop变量
loop.index  序号从1开始
loop.index0  序号从0开始

loop.revindex  reverse  序号是倒着的
loop.revindex0

loop.first 布尔类型   是否是第一行
loop.last  布尔类型   是否是第二行

3。过滤器
过滤器的本质就是函数
模板语法中过滤器：
{{ 变量名 | 过滤器(*args) }}

{{ 变量名 | 过滤器 }}

常见的过滤器：
1。 safe ： 禁用转译
msg = '<h1>520快乐！</h1>'
return render_template('show_2.html', girls=girls, users=users, msg=msg)
不想让其转译：
{{ msg | safe }}
2。 capitalize：单词的首字母大写
{{ n1 | capitalize }}
3。lower和upper
大小写的转换
4。title 一句话中每个单词的首字母大写
 msg = 'She is a beautiful girl'
 {{ msg | title}}
5。reverse  翻转
{{ n1 | reverse}}
6。format
{{ '%s is %d years old' | format('lily',18) }}
7.truncate 字符串截断

list的操作：
{# 列表过滤器的使用 #}
{{ girls | first }}<br>
{{ girls | last }}<br>
{{ girls | length }}<br>
{#{{ girls | sum }} 整型的计算 #}
{{ [1,3,5,7,9] | sum }}<br>
{{ [1,8,5,7,3] | sort }}<br>


dict:
{% for v in users.0.values() %}   ---->获取值
    <p>{{ v }}</p>
{% endfor %}

<hr>
{% for k in users.0.keys() %}   ----》获取键
    <p>{{ k }}</p>
{% endfor %}

<hr>

{% for k,v in users.0.items() %}  ---》获取键值
    <p>{{ k }}---{{ v }}</p>
{% endfor %}














