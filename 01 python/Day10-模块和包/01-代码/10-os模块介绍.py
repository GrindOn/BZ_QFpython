# os全称 OperationSystem操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name ==> 获取操作系统的名字    windows系列 ==>nt / 非windows ==>posix
print(os.name)  # nt
print(os.sep)  # 路径的分隔符  windows \   非windows /

# os模块里的 path 经常会使用
# abspath ==> 获取文件的绝对路径
print(os.path.abspath('01-高阶函数.py'))

# isdir判断是否是文件夹
print(os.path.isdir('02-函数的嵌套.py'))  # False
print(os.path.isdir('xxx'))  # True

# isfile 判断是否是文件
print(os.path.isfile('03-闭包的概念.py'))  # True
print(os.path.isfile('xxx'))  # False

# exists 判断是否存在
print(os.path.exists('05-优化计算时间的代码.py'))  # True
print(os.path.exists('mmm.py'))  # False

file_name = '2020.2.21.demo.py'
# print(file_name.rpartition('.'))
print(os.path.splitext(file_name))

# os里其他方法的介绍
# os.getcwd()  # 获取当前的工作目录，即当前python脚本工作的目录
# os.chdir('test') # 改变当前脚本工作目录，相当于shell下的cd命令
# os.rename('毕业论文.txt','毕业论文-最终版.txt') # 文件重命名
# os.remove('毕业论文.txt') # 删除文件
# os.rmdir('demo')  # 删除空文件夹
# os.removedirs('demo') # 删除空文件夹
# os.mkdir('demo')  # 创建一个文件夹
# os.chdir('C:\\') # 切换工作目录
# os.listdir('C:\\') # 列出指定目录里的所有文件和文件夹
# os.name # nt->widonws posix->Linux/Unix或者MacOS
# os.environ # 获取到环境配置
# os.environ.get('PATH') # 获取指定的环境配置
