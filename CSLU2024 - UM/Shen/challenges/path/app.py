from flask import Flask, request
import requests
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    path = request.args.get("path")

    if path == None:
        return "SSRF usage is /?path=/page"
    
    if path == "/flag":
        return "Flag stealer detected!"
    
    response = requests.get(f"http://localhost:5003{path}")
    
    return response.text

@app.route('/internal')
def internal():
    client_ip = request.remote_addr

    if client_ip != "127.0.0.1":
        return "Path is restricted to admins!"
    
    return "Internal service reached!"

@app.route('/flag')
def flag():
    client_ip = request.remote_addr

    if client_ip != "127.0.0.1":
        return "Path is restricted to admins!"
    
    return "flag{fake_flag}"
    
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5003)
