主要理解多张数据库表的关系。

明确：一个项目肯定会有多张表，确定表与表之间的关系最重要。
在开始项目前必须要确定表与表的关系

单独一张表： User 是不行的。user要与其他的建立联系。

以student和班级clazz为例：
一个班级是有多名学生的

----模板
     --html
     --js
     --css
     --images

使用flask-bootstrap:
步骤：
1。pip install flask-bootstrap
2.进行配置：
 from flask-bootstrap import Bootstrap
 bootstrap = Bootstrap()

 在__init__.py中进行初始化：
 # 初始化bootstrap
 bootstrap.init_app(app=app)
3。内置的block：
  {% block title %}首页{% endblock %}

{% block navbar %} {% endblock %}

{% block content %} {% endblock %}

{% block styles %} {% endblock %}

{% block srcipts %} {% endblock %}
{% block head %} {% endblock %}

{% block body %} {% endblock %}


flask-bootstrap
bootstrap-flask  -----> 卸载

