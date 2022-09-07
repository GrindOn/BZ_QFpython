from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = '沈凯'  # str
    age = 18  # int
    friends = ['建义', '陈璟', '小岳岳', '郭麒麟']  # list
    dict1 = {'gift': '大手镯', 'gift1': '鲜花', 'gift2': '费列罗'}  # dict
    # 创建对象
    girlfriend = Girl('美美', '安徽阜阳')
    return render_template('show.html', name=name, age=age, gender='男', friends=friends, dict1=dict1, girl=girlfriend)


# 则以空白字符串填充"


#


if __name__ == '__main__':
    app.run()
