from flask import Flask, render_template, request, url_for, redirect
#from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mariadb'
app.config['MYSQL_DB'] = 'movies'

mysql = MySQL(app)
#mysql = SQLAlchemy(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rent")
    rv = cur.fetchall()
    cur.close()
    return render_template('data.html', rent=rv)

if __name__ == '__main__':
    app.run(debug=True)