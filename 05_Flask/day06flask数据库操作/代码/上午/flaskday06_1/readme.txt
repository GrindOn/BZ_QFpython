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

  and or  order_by like ....


 总结：
 1. User.query.all()  所有
 2. User.query.get(pk)  一个
 3. User.query.filter()   *   ？？？？？？？
 4. User.query.filter_by()


 删除  更新

 两张表