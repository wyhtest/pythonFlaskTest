from flask import render_template
from app.info import info

@info.app_errorhandler(404)
def page_not_found(e):
    return render_template('info/404.html'),404

@info.app_errorhandler(500)
def internal_server_error(e):
    return render_template('info/500.html'),500