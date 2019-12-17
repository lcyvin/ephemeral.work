from flask import Flask, render_template, request
from lib.users import User
app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    lc = request.args.get('lc')
    if not lc:
        lc = 'en'
    user = User(locale=lc)
    return render_template(
        'base/index.html',
        user=user,
        locale=user.locale.page('index')
        )
