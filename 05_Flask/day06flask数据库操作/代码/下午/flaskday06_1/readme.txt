1.查询：
查询所有： 模型类.query.all()    ~  select * from user;
如果有条件的查询：
         模型类.query.filter_by(字段名 = 值)   ～  select * from user where 字段=值；
         模型类.query.filter_by(字段名 = 值).first()   ～  select * from user where 字段=值 limit..；

select * from user where age>17 and gender='男'；
select * from user where username like 'zhang%';
select * from user where rdatetime> xxx and rdatetime < xxx;

         模型类.query.filter()  里面是布尔的条件   模型类.query.filter(模型名.字段名 == 值)
         模型类.query.filter_by()  里面是一个等值   模型类.query.filter_by(字段名 = 值)


***** 模型类.query.filter() ******
1. 模型类.query.filter().all()   -----> 列表
2. 模型类.query.filter().first()  ----->对象
3.User.query.filter(User.username.endswith('z')).all()   select * from user where username like '%z';
  User.query.filter(User.username.startswith('z')).all()  # select * from user where username like 'z%';
  User.query.filter(User.username.contains('z')).all()  # select * from user where username like '%z%';
  User.query.filter(User.username.like('z%')).all()

  多条件：
  from sqlalchemy import or_, and_,not_
  并且： and_    获取： or_   非： not_
  User.query.filter(or_(User.username.like('z%'), User.username.contains('i'))).all()
   类似： select * from user where username like 'z%' or username like '%i%';

  User.query.filter(and_(User.username.contains('i'), User.rdatetime.__gt__('2020-05-25 10:30:00'))).all()
   # select * from user where username like '%i%' and rdatetime < 'xxxx'

  补充：__gt__,__lt__,__ge__(gt equal),__le__ （le equal）  ----》通常应用在范围（整型，日期）
       也可以直接使用 >  <  >=  <=  !=

  User.query.filter(not_(User.username.contains('i'))).all()

  18 19 20 17 21 22 ....
  select * from user where age in [17,18,20,22];


排序：order_by

    user_list = User.query.filter(User.username.contains('z')).order_by(-User.rdatetime).all()  # 先筛选再排序
    user_list = User.query.order_by(-User.id).all()  对所有的进行排序
    注意：order_by(参数)：
    1。 直接是字符串： '字段名'  但是不能倒序
    2。 填字段名： 模型.字段    order_by(-模型.字段)  倒序

限制： limit
    # limit的使用 + offset
    # user_list = User.query.limit(2).all()   默认获取前两条
    user_list = User.query.offset(2).limit(2).all()   跳过2条记录再获取两条记录


 总结：
 1. User.query.all()  所有
 2. User.query.get(pk)  一个
 3. User.query.filter()   *   ？？？？？？？
     如果要检索的字段是字符串（varchar，db.String）:
       User.username.startswith('')
       User.username.endswith('')
       User.username.contains('')
       User.username.like('')
       User.username.in_(['','',''])
       User.username == 'zzz'
    如果要检索的字段是整型或者日期类型：
       User.age.__lt__(18)
       User.rdatetime.__gt__('.....')
       User.age.__le__(18)
       User.age.__ge__(18)
       User.age.between(15,30)

     多个条件一起检索： and_, or_
     非的条件： not_

     排序：order_by()
     获取指定数量： limit() offset()
 4. User.query.filter_by()


 删除:
 两种删除：
 1。逻辑删除（定义数据库中的表的时候，添加一个字段isdelete，通过此字段控制是否删除）
 id = request.args.get(id)
 user = User.query.get(id)
 user.isdelete = True
 db.session.commit()

 2。物理删除(彻底从数据库中删掉)
 id = request.args.get(id)
 user = User.query.get(id)
 db.session.delete(user)
 db.session.commit()


 更新:
 id = request.args.get(id)
 user = User.query.get(id)
 # 修改对象的属性
 user.username= xxxx
 user.phone =xxxx
 # 提交更改
 db.session.commit()


 两张表