# app.py
from flask import Flask, redirect, url_for, render_template, request, flash, Response

import os
from os.path import join, dirname
import gnupg
import json
import datetime

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 4567))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    data = {"event": request.form['event'], "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    
    with open("log.txt", "a") as f:
        f.write(str(gnupg.GPG().encrypt(json.dumps(data), os.environ.get('MEDLOG_KEY', "redhog@redhog.org"))))
        f.write("\n\n")
        
    return redirect(url_for('index'))

@app.route('/log', methods=['GET'])
def log():
    with open("log.txt") as f:
        return Response(f.read(), content_type="text/plan")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
    
