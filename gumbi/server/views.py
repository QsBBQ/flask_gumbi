from flask import render_template

from gumbi.server import app

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')
