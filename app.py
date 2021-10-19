# app.py
from flask import Flask, redirect, url_for, render_template, request, flash, Response

import os.path
import gnupg
import json
import datetime

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 4567))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/', methods=['POST'])
def index_post():
    now = datetime.datetime.now()

    event = request.form['event']
    if event == "custom":
        event = request.form['event-custom']
    event_time = report_time = now.strftime("%Y-%m-%d %H:%M:%S")
    if request.form.get("custom-time"):
        event_time = request.form["time"].strip()
    data = {"event": event, "report-time": report_time, "event-time": event_time}
    filename = "log-%s-%s.txt" % (now.year, now.month,)
    
    print("%s: %s" % (filename, data))
    
    with open(filename, "a") as f:
        f.write(str(gnupg.GPG().encrypt(json.dumps(data), os.environ.get('MEDLOG_KEY', "redhog@redhog.org"))))
        f.write("\n\n")
        
    return redirect(url_for('index'))

@app.route('/log/', methods=['GET'])
def log():
    months = [name.split(".")[0].split("-", 1)[1] for name in os.listdir() if name.startswith("log-") and name.endswith(".txt")]
    return render_template('logs.html', months=months)

@app.route('/log/<month>', methods=['GET'])
def logs(month):
    month = int(month)
    with open("log-%s.txt" % (month,)) as f:
        return Response(f.read(), content_type="text/plan")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
    
