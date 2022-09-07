web阶段：知识的融合
mvc  mtv

虚拟环境：
pip install virtualenv
pip install virtualenvwrapper-win

虚拟环境常用命令：
mkvirtualenv 虚拟环境名字
lsvirtualenv  查看所有的虚拟环境名称
cdvirtualenv  切换到当前的虚拟环境目录下
rmvirtualenv  虚拟环境名字   ----》删除虚拟环境
workon 虚拟环境名字  ----》虚拟环境之间切换



1. pip3 list
原因： 当初创建项目的时候已经指定了flask，所以pycharm在创建项目的时候会自动执行: pip install flask

2. 自己安装：
进入终端中进入虚拟环境-----> pip list

pip install pymysql

pip install flask==1.0 (卸载原来的版本，安装指明的版本)

3. 项目结构介绍：

--项目名：
   |---static （静态）js css
   |---templates （模板）
   |---app.py (运行|启动)

web项目：
   mvc：
   model 模型
   view  视图
   controler 控制器


python：
   mtv:
   model 模型
   template 模板 ---》html
   view 视图  起控制作用  python代码


b/s:
browser 浏览器
server：服务器



c/s:
client  客户端
server  服务器

(flask01) runningdeMacBook-Pro-2:flaskday01_1 running$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


app = Flask(__name__)

run(host='ip地址'，port='端口号')

ip地址，一个端口号对应的是一个程序

http://192.168.1.5:5000/
如果host改成：0.0.0.0  外网可以访问
默认情况下只能是本机。

app.run(host='0.0.0.0', port=5001, debug=True)
debug: 布尔类型的
debug=True  开启了debug调试模式  只要代码改变服务器会重新加载最新的代码  适用于开发环境development
debug=False  默认  代码发生改变不会自动加载  适用于production环境

环境：
production
development
testing


设置配置文件：
settings
# 配置文件
ENV = 'development'
DEBUG = True


路由的请求和响应：

浏览器地址栏输入的内容： http://192.168.1.5:8000/index   ---->服务器 ----->app ----->有没有这个路由
---->就会执行路由匹配的函数 ------> return 'hello world'  -----> response ------>客户端的浏览器

请求：request
http协议：
request 请求
请求行 ： 请求地址： http://0.0.0.0:8000/index
        请求方法是什么？ method： get  post
请求头： key:value
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Host: 0.0.0.0:8000
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
请求体:



response 响应
响应行: 状态码  200 ok ， 404  not found ，500  ，302， ？？？？作业
响应头：
Content-Length: 18
Content-Type: text/html; charset=utf-8
Date: Mon, 18 May 2020 08:57:02 GMT
Server: Werkzeug/1.0.1 Python/3.7.4
响应体：
<font color="red"> Hello World333333! </font>

flask文档：
https://dormousehole.readthedocs.io/en/latest/
















