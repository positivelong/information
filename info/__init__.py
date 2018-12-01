from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from config import config
from flask import Flask

app = Flask(__name__)
# 加载配置
app.config.from_object(config["development"])
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=config["development"].REDIS_HOST, port=config["development"].REDIS_PORT)
# 开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)
Session(app)