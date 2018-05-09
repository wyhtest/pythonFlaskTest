from flask import Flask,render_template
from app.main import main
from app.info import info
from flask_bootstrap import  Bootstrap
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['SECRET_KEY']='hellow'
bootstrap = Bootstrap(app)
app.config.from_object(config)
db = SQLAlchemy(app)
#创建表
class Article(db.Model):#继承db.Model
    __tablemame__='article'#表名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
db.create_all() #执行





@app.route('/')
def index():

    # # 增加：
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # # 事务
    # db.session.commit()

    # # 查
    # # select * from article where article.title='aaa';
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    #
    # print ('title:%s' % article1.title)
    # print('content:%s' % article1.content)
    article1 = Article.query.all()
    for u in article1:

        print(u.id, u.title, u.content)

    # # 改：
    # # 1. 先把你要更改的数据查找出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2. 把这条数据，你需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3. 做事务的提交
    # db.session.commit()


    # # 删
    # # 1. 把需要删除的数据查找出来
    # article1 = Article.query.filter(Article.content == 'bbb').first()
    # # 2. 把这条数据删除掉
    # db.session.delete(article1)
    # # 3. 做事务提交
    # db.session.commit()

    # # 自定义
    # ret = db.session.execute('select * from article')
    # print (ret)
    return render_template('index.html'),200

app.register_blueprint(main,url_prefix='/hello')

app.register_blueprint(info,url_prefix='/hi')
if __name__ == '__main__':
    app.run(debug=True);