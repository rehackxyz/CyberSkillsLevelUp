from flask import Flask, request, render_template, redirect, session
import mysql.connector
import os
from waitress import serve


app = Flask(__name__)
app.secret_key = os.urandom(32)

CONFIG = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'port': '3306',
        'database': 'levelup'
}

@app.route('/', methods = ["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template('index.html')
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(**CONFIG)
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = BINARY %s"
        cursor.execute(query, (username, password))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        if results:
            session['valid'] = True
            return redirect(f'/flag')
        else:
            error = "Invalid username or password."
            return render_template(f'index.html', error=error)

    
    
@app.route('/search', methods = ["GET"])
def search():
    name = request.args.get("name", "")
    
    # Fixing original SQLi query, I disabled GET method for now, it is safe, they can't abuse it.
    if request.method == "GET":
        error = "Toy search disabled due to SQLi abused by hackers."
        return render_template('search.html', error=error)

    try:
        conn = mysql.connector.connect(**CONFIG)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM toys WHERE name = '{name}'")
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    except:
        return "Error occured"
    
@app.route('/flag')
def flag():
    if not session:
        return redirect('/')
    
    return render_template('flag.html', flag="flag{fake_flag}")

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5002)