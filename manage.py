import logging

from flask import current_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db

"""
manane.py 是程序启动的入口, 只关心启动的相关参数以及内容,不关心具体
该如何创建app或者相关业务逻辑
"""

# 通过指定的配置名字创建对应配置的app
# create_app 就类似于工厂方法
app = create_app('development')
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

# @app.route('/')
# def index():
#
#     # 测试打印日志
#     logging.debug('测试debug')
#     logging.warning('测试warning')
#     logging.error('测试error')
#     logging.fatal('测试fatal')
#     # Flask 中打印日志的方法
#     current_app.logger.error("测试error11")
#     return 'index测试代码'

if __name__ == '__main__':
    manager.run()