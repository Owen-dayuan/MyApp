﻿import io
from flask import Flask, render_template, g #, request, session, redirect, url_for, abort

app = Flask(__name__)
app.config.from_pyfile('../conf/config.py')

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

if __name__ == '__main__':
    app.run()