

# dialect+driver://username:password@host:port//database
# 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'welcome'
HOST = '127.0.0.1'
PORT = '3307'
DATABASE ='pythontest'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True