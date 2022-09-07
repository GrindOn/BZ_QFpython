class Student(object):
    def __init__(self, number, name, age, gender, score):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return '编号:{},姓名:{},年龄:{},性别:{},分数{}'.format(self.number, self.name, self.age, self.gender,
                                                     self.score)


class Grade(object):
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def show_all(self):
        for student in self.students:
            print(student)

    def get_student_by_number(self, n):
        for s in self.students:
            if s.number == n:
                return s
        else:
            return '用户未找到'

    def failed_students(self):
        result = filter(lambda student: student.score < 60, self.students)
        for x in result:
            print(x)

    def order_students(self):
        # self.students.sort(key=lambda s: s.score, reverse=True)  # 直接修改self.students
        return sorted(self.students, key=lambda s: s.score, reverse=True)


# 如果数字以 0 开头，在Python2里表示八进制
s1 = Student(1, 'zhangsan', 18, 'male', 80)
s2 = Student(5, '李四', 19, 'male', 50)
s3 = Student(10, 'tony', 20, 'male', 70)
s4 = Student(7, 'jack', 18, 'female', 90)
s5 = Student(4, 'henry', 19, 'female', 56)

g = Grade('中二班', [s1, s2, s3, s4, s5])
# g.show_all()
# g.failed_students()
# x = g.order_students()
# for student in x:
#     print(student)


print(g.get_student_by_number(1))

