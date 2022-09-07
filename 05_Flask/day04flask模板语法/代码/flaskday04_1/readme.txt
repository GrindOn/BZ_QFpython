回顾：
视图：
request
request.method ----> app.url_map
request.args
request.form
...

response
1. 字符串
2. 字典
3. tuple
4. response对象
5. make_response()
6. render_template()
7. redirect()  --->  response  重定向


render_template('模板名字',**context)

render_template('模板名字',name=name,age=age,...)

模板语法：
1.变量
{{ name }}
{{ age }}

字符串
列表
tuple
set
对象 ----> [s1,s2,s3]
    ----->[{},{},{}]

2.过滤器： 本质就是函数

{{ name | length }}
{{ users | first }}

3. 控制块

{% if 条件 %}

{% endif %}

{% if 条件 %}
    pass
{% else %}
    pass
{% endif %}

{% if 条件 %}
    pass
{% elif 条件 %}
    pass
 ....
{% endif %}

{% for 变量 in 可迭代 %}
   {{ loop.index }}
{% endfor %}


今天：模板
1. 自定义过滤器：

# 过滤器本质就是函数
1. 通过flask模块中的add_template_filter方法
    a. 定义函数，带有参数和返回值
    b. 添加过滤器  app.add_template_filter(function,name='')
    c. 在模板中使用： {{ 变量 | 自定义过滤器 }}
2。使用装饰器完成
    a. 定义函数，带有参数和返回值
    b. 通过装饰器完成，@app.template_filter('过滤器名字')装饰步骤一的函数
    c. 在模板中使用： {{ 变量 | 自定义过滤器 }}


模板：复用
模板继承 *
include
宏


模板继承：
需要模版继承的情况：
1。 多个模板具有完全相同的顶部和底部
2。 多个模板具有相同的模板内容，但是内容中部分不一样
3。 多个模板具有完全相同的模板内容

标签：
{% block 名字 %}

{% endblock %}

1.定义父模板
2.子模板继承父模板
步骤：
父模板：
1。 定义一个base.html的模板
2。 分析模板中哪些是变化的比如：{% block title %}父模板的title{% endblock %}
    对变化的部分用block进行"预留位置"也称作：挖坑
3。注意：样式和脚本 需要提前预留
    {% block mycss %}{% endblock %}
    {% block myjs %}{% endblock %}

子使用父模板：
1。 {% extends '父模板的名称' %}将父模板继承过来
2。 找到对应的block（坑）填充，每一个block都是有名字的。


include: 包含
在A，B，C页面都共同的部分，但是其他页面没有这部分。
这个时候考虑使用include
步骤：
1。先定义一个公共的模板部分,xxx.html
2。谁使用则include过来， {% include '文件夹/xxx.html' %}


宏：macro
1。把它看作是jinja2的一个函数，这个函数可以返回一个HTML字符串
2。目的：代码可以复用，避免代码冗余

定义两种方式：
1。在模板中直接定义：
    类似： macro1.html  中定义方式
2。将所有宏提取到一个模板中：macro.html
   谁想使用谁导入：
   {% import 'macro.html' as xxx %}
   {{ xxx.宏名字(参数) }}

总结：
变量： {{ 变量 }}
块：
{% if 条件 %} ....{% endif %}
{% for 条件 %} ....{% endfor %}
{% block 条件 %} ....{% endblock %}
{% macro 条件 %} ....{% endmacro %}

{% include '' %}  包含
{% import '' %}    导入宏
{% extends '' %}

{{ url_for('static',filename='') }}
{{ hongname(xxx) }}


view:
@app.route('/',endpoint='',methods=['GET','POST'])
def index():
    直接使用request
    return response|''|render_template('xxx.html')

template:
  模板的语法

model：





