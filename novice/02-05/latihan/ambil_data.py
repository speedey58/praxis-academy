import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb",
    database="keluarga"
)

cursor = db.cursor()
sql = "SELECT * FROM profil"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)