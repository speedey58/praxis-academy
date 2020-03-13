import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb",
    database="motogp"
)

cursor = db.cursor()
sql = """CREATE TABLE pebalap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomor Varchar(2),
    nama Varchar(15),
    motor Varchar(10)
)
"""
#cursor.execute(sql)

cursor = db.cursor()
sql = "INSERT INTO pebalap (nomor, nama, motor) VALUES (%s, %s, %s)"
values = [
    ("46","Rossi","Yamaha"),
    ("93","Marquez","Honda"),
    ("04","Dovizioso","Ducati"),
    ("42","Rins","Suzuki"),
    ("55","Syahrin","KTM")
]

for val in values:
    cursor.execute(sql, val)
    #db.commit()

cursor = db.cursor()
sql = "SELECT * FROM pebalap"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)