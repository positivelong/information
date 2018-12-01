import redis
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect

class Config(object):
    """工程的配置信息"""
    SECRET_KEY = "2lqQ1UzupwqovcYtwrY34XixIooiPGVH39N9MwGVyW8MpERIv4F9ce0emy1Y7E9n"

    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information_09"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session的配置信息
    SESSION_TYPE = "redis" # 指定session 保存到redis 中
    SESSION_USE_SIGNER = True # 让cookie中的session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host= REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期, 单位是秒
    SESSION_PERMANENT = False  # 设置需要过期


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)
Session(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return 'index测试代码'

if __name__ == '__main__':
    manager.run()