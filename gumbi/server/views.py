from flask import render_template
import json
from gumbi.server import app
from gumbi.db.database import db_session as s, init_db
from gumbi.db.models import User, Widget, Planet
from gumbi.util.loader import MyTest

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/table')
def table():
    #return 'Hello, World!'
    users = s.query(User).all()
    users_list = [{'name': user.name, 'email': user.email} for user in users]
    # print(test)
    # for user in users:
    #     print(user.name)
    MyTest().show_test()
    return render_template('table.html', users=users_list)
