from flask import Flask, render_template, request
from waitress import serve
import os

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', query="")
    
    elif request.method == "POST":
        command = request.form["command"]
        if not command:
            return render_template('index.html', query="No command issued!")
        else:
            os.system(command)
            return render_template('index.html', query="Executed command!")
    
    return "Method not allowed"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
