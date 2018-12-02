import logging

import redis



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

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG

class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True
class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING
class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
