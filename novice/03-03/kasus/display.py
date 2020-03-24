from flask import Flask, render_template, request
import mysql.connector as mariadb

app = Flask(__name__)

@app.route('/')
def list():
    conn = mariadb.connect(user='root', password='mariadb', database='movies')

    cur = conn.cursor()
    cur.execute("SELECT * FROM rent")
    rows = cur.fetchall()
    cur.close()
    return render_template('data.html',rent=rows)

if __name__=='__main__':
    app.run(debug = True)