from flask import Flask,render_template
from app.main import main
from app.info import info
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
import pymysql

#app.config['SECRET_KEY']='hellow'
bootstrap = Bootstrap()
#app.config.from_object(config)
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    app.register_blueprint(main)

    app.register_blueprint(info,url_prefix='/hi')
    return  app



# #创建表
# class Article(db.Model):#继承db.Model
#     __tablemame__='article'#表名
#     id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     title = db.Column(db.String(100),nullable=False)
#     content = db.Column(db.Text,nullable=False)
# db.create_all() #执行


# conn = pymysql.Connect(host='127.0.0.1',port=3307,user='root',passwd='welcome',db='pythontest',charset='utf8')
# cursor = conn.cursor()
# sql = 'select * from person'
# cursor.execute(sql)
# # rs = cursor.fetchone()
# # print("rs:",rs)
# #
# # for each in cursor.fetchmany(2):
# #     print(each)
# # print()
# for each in cursor.fetchall():
#     print(each)



# @app.route('/')
# def index():
#     ret = db.session.execute("select *  from person  where id = '1'")
#     print (ret)
#     return render_template('index.html'),200
#
# app.register_blueprint(main,url_prefix='/hello')
#
# app.register_blueprint(info,url_prefix='/hi')
# if __name__ == '__main__':
#     app.run(debug=True);
