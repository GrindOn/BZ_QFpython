from flask import Flask
from flask_script import Manager

from apps import create_app

app = create_app()

manager = Manager(app=app)


@manager.command
def init():
    print('初始化')


if __name__ == '__main__':
    manager.run()
