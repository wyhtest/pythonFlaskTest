from . import info,forms
from flask import render_template

@info.route('/info/', methods=['GET', 'POST'])
def info():
    form = forms.myForm()
    if form.validate_on_submit():
        return render_template('info/welcome.html'),200;
    return render_template('info/main.html',form = form),200
