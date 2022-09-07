主要理解多张数据库表的关系。

明确：一个项目肯定会有多张表，确定表与表之间的关系最重要。
在开始项目前必须要确定表与表的关系

单独一张表： User 是不行的。user要与其他的建立联系。

以student和班级clazz为例：
一个班级是有多名学生的

![](/Users/running/Desktop/屏幕快照 2020-05-26 下午12.39.04.png)

如果是sql语句：

1. 查询python01班级的学生

   ```sql
   select * from student where 班级=（select id from clazz where 班级名=‘python01’）
   或者
   select * from student inner join clazz on student.班级=clazz.id where clazz.班级名='python01' 
   ```

   

2. 查询xiaowang所在的班级名

   ```sql
   select 班级名 from clazz where id= (select 班级 from student where name='xiaowang')
   或者
   select 班级名 from student inner join clazz on student.班级=clazz.id where name='xiaowang'
   ```

   

但是体现在python框架中不方便直接写表连接查询和子查询。python框架为了简化多表的查询，制定了多表的关系：

1. 1对多

   常见的比如：班级对学生，部门对员工，学校对班级，用户对文章，用户对订单

   可以说一个班级有多名同学或者一个部门有多名员工，但是不能说：

   一一个员工属于多个部门，一个班级属于多个学校....

   > 在flask的框架中如何体现1对多的模型关系？
   >
   > 就是通过外键ForignKey和relationship体现。ForignKey是给映射关系说的，relationship是给模板使用的。

   ```python
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True, autoincrement=True)
       username = db.Column(db.String(15), nullable=False)
       password = db.Column(db.String(64), nullable=False)
       phone = db.Column(db.String(11), unique=True, nullable=False)
       email = db.Column(db.String(30))
       icon = db.Column(db.String(100))
       isdelete = db.Column(db.Boolean, default=False)
       rdatetime = db.Column(db.DateTime, default=datetime.now)
       # 增加一个字段
       articles = db.relationship('Article', backref='user')
       #
       def __str__(self):
           return self.username
   ```

   ```python
   from datetime import datetime
   
   from exts import db
   
   
   class Article(db.Model):
       id = db.Column(db.Integer, primary_key=True, autoincrement=True)
       title = db.Column(db.String(50), nullable=False)
       content = db.Column(db.Text, nullable=False)
       pdatetime = db.Column(db.DateTime, default=datetime.now)
       click_num = db.Column(db.Integer, default=0)
       save_num = db.Column(db.Integer, default=0)
       love_num = db.Column(db.Integer, default=0)
       # 外键 同步到数据库的外键关系
       user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   
   ```

   

2. 多对多

   常见的多对多：用户对文章评论，用户对商品，学生对课程

   一个用户可以买多个商品，反过来这个个学生属于多个班级，商品的还可以让多个用户购买
   
   用户 1 -----》 n 商品
     n  《-----  1

   一个学生可以选择多门课程，反过来一门课程还可以让多个学生选择

   ....

   ```python
   tags = db.Table('tags',
       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
       db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
   )
   
   class Page(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       tags = db.relationship('Tag', secondary=tags,
           backref=db.backref('pages', lazy='dynamic'))
   
   class Tag(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(20),nullable=False)
   ```

或者

​	

```python
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary='Page_tag',
        backref='pages')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    
class Page_tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'))
```

大家可以尝试分析：
微信中可能涉及的表以及关系。 比如： 用户与好友之间的关系？？？ 
user ----》  friend
订票网站中： 电影与用户的关系
电影goods  user

class User(db.Model):
    xxxx
    articles = db.relationship('Article',backref='user')

class Article(db.Model):
    xxxx
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))   ----->在多这方添加外键
    # user = db.relationship('User',backref='articles')
....
