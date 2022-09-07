

1. 创建项目并设置settings.py文件

2. 删除app.py中的部分内容

3. 创建包apps,并在包中__init__.py中创建app的工厂函数

   ```python
   def create_app():
       app = Flask(__name__)  # app是一个核心对象
       app.config.from_object(settings)  # 加载配置
       # 蓝图
       return app
   ```

   

4. 在apps中创建项目的程序包比如user，goods，order等

5. 以user为例，在user包中创建view.py，在view.py中定义蓝图

   ```python
   user_bp = Blueprint('user', __name__)
   # 	其中第一个参数是蓝图的名字，第二个参数是import_name
   ```

   

6. 使用蓝图定义路由和视图函数

   ```python
   @user_bp.route('/')
   def user_center():
       return render_template('user/show.html', users=users)
   ```

   注意在蓝图中进行了模板的加载，而模板的文件夹默认是跟flask对象是同级的，如果不是同级的注意在Flask对象创建的时候初始化设置

   

7. 注册蓝图到app对象上

   ```python
   def create_app():
       app = Flask(__name__,template_folder='../templates',static_folder='../static')  # app是一个核心对象
       app.config.from_object(settings)  # 加载配置
       # 蓝图
       app.register_blueprint(user_bp)  # 将蓝图对象绑定到app上
   
       print(app.url_map)
   
       return app
   ```

8. 补充删除操作的步骤：

-   点击删除按钮或者删除链接

-   给链接添加单击事件，可以通过js或者jquery

  ```python
   <a href="javascript:;" onclick="del('{{ user.username }}')">删除</a>
  ```

  

-   在js中定义函数：

  ```javascript
   function del(username){
              // console.log(username)
              // location 地址栏对象
              location.href = '/del?username='+username
          }
  ```

  

- 触发/del的路由函数

  ```python
  @user_bp.route('/del')
  def del_user():
      # 获取你传递的username
      username = request.args.get('username')
      # 根据username找到列表中的user对象
      for user in users:
          if user.username == username:
              # 删除user
              users.remove(user)
              return redirect('/')
      else:
          return '删除失败'
  ```

  