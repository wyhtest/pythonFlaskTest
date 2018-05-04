from flask import Flask,render_template
from app.main import main
from app.info import info
from flask_bootstrap import  Bootstrap
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']='hellow'
bootstrap = Bootstrap(app)
db = SQLAlchemy()
@app.route('/')
def index():
    return render_template('index.html'),200

app.register_blueprint(main,url_prefix='/hello')

app.register_blueprint(info,url_prefix='/hi')
if __name__ == '__main__':
    app.run(debug=True);