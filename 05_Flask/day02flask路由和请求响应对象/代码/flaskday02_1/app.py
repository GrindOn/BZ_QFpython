from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)


# add_url_rule与装饰器的关系
@app.route('/')
def hello_world():
    return 'Hello World!'


def index():
    return 'welcome everyone！'


app.add_url_rule('/index', view_func=index)

if __name__ == '__main__':
    app.run()
