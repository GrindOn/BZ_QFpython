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



