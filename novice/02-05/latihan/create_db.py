import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE motogp")

print("Database berhasil dibuat")