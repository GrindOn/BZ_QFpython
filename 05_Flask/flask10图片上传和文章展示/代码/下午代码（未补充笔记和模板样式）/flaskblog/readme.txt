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
--- 5.27 ---
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

密码加密：
注册：
generate_password_hash(password)  ----> 加密后的密码
sha256加密$salt$48783748uhr8738478473...

登录：
check_password_hash(pwdHash,password)  -----> bool:False,True

会话机制：
1。cookie方式：

  保存：
    通过response对象保存。
    response = redirect(xxx)
    response = render_template(xxx)
    response = Response()
    response = make_response()
    response = jsonify()
    # 通过对象调用方法
    response.set_cookie(key,value,max_age)
    其中max_age表示过期时间，单位是秒
    也可以使用expires设置过期时间，expires=datetime.now()+timedelta(hour=1)

  获取：
    通过request对象获取。
    request.form.get()
    request.args.get()
    cookie也在request对象中
    request.cookies.get(key) ----> value

  删除：
     通过response对象删除。 把浏览器中的key=value删除了
    response = redirect(xxx)
    response = render_template(xxx)
    response = Response()
    response = make_response()
    response = jsonify()
    # 通过对象调用方法
    response.delete_cookie(key)

2。session：  是在服务器端进行用户信息的保存。一个字典
注意：
使用session必须要设置配置文件，在配置文件中添加SECRET_KEY='xxxxx'，
添加SECRET_KEY的目的就是用于sessionid的加密。如果不设置会报错。

  设置：
    如果要使用session，需要直接导入：
    from flask import session

    把session当成字典使用，因此：session[key]=value
    就会将key=value保存到session的内存空间
    **** 并会在响应的时候自动在response中自动添加有一个cookie：session=加密后的id ****
  获取
     用户请求页面的时候就会携带上次保存在客户端浏览器的cookie值，其中包含session=加密后的id
     获取session值的话通过session直接获取，因为session是一个字典，就可以采用字典的方式获取即可。
     value = session[key] 或者 value = session.get(key)
     这个时候大家可能会考虑携带的cookie怎么用的？？？？
     其实是如果使用session获取内容,底层会自动获取cookie中的sessionid值，
     进行查找并找到对应的session空间

   删除
    session.clear()  删除session的内存空间和删除cookie
    del session[key]  只会删除session中的这个键值对，不会删除session空间和cookie


secretID：dcc535cbfaefa2a24c1e6610035b6586
secretKey：d28f0ec3bf468baa7a16c16c9474889e
bid ：748c53c3a363412fa963ed3c1b795c65

---- 5.28 -----

1.短信息发送：


2.登录权限的验证
只要走center路由，判断用户是否是登录状态，如果用户登录了，可以正常显示页面，如果用户没有登录
则自动跳转到登录页面进行登录，登录之后才可以进行查看。

钩子函数：
直接应用在app上：
before_first_request
before_request
after_request
teardown_request

应用到蓝图：
before_app_first_request
before_app_request
after_app_request
teardown_app_request

3.文件上传


