from . import main
from flask import render_template

@main.route('/test/')
def test():
    return render_template('main/test.html'),200