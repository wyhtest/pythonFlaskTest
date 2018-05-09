from . import db

class Article(db.Model):#继承db.Model
    __tablemame__='article'#表名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.title
