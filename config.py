# dialect+driver://username:password@host:port//database
# 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'
# DIALECT = 'mysql'
# DRIVER = 'pymysql'
# USERNAME = 'root'
# PASSWORD = 'welcome'
# HOST = '127.0.0.1'
# PORT = '3307'
# DATABASE ='pythontest'
#
# SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_COMMIT_TEARDOWN = True
import os
basedir = os.path.abspath(os.path.dirname(__file__)) #当前文件所在的路径

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'python python hahaha'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #设置是否在每次连接结束后自动提交数据库中的变动。
    SQLALCHEMY_TRACK_MODIFICATIONS = True#如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存，如果不必要的可以禁用它
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'welcome'
    HOST = '127.0.0.1'
    PORT = '3307'
    DATABASE ='pythontest'

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}

