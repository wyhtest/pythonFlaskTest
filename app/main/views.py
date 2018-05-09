from . import main
from flask import render_template


@main.route('/')
def index():

    return render_template('index.html'), 200
@main.route('/test/')
def test():
    return render_template('main/test.html'),200