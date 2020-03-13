## Instalasi Mariadb Connector
Install MariaDB connector menggunakan pip sebagai berikut:
```
pip3 install mysql-connector
```
tunggu hingga proses download selesai

## Koneksi ke MySQL dari python
buat file baru **connect.py** sebagai berikut
```
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb"
)

if db.is_connected():
    print("Berhasil terhubung ke database"
    )
```
host diisikan "localhost", user diisikan "root", passwd diisikan pasword untuk mengakses database. Jalankan file python di atas, jika koneksi sukses akan muncul **Berhasil terhubung ke database**.

## Mengambil data MySQL dari python
kita akan mengambil data yang dibuat dari latihan sebelumnya di MariaDB

```
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
```

## Membuat database MySQL dari python 
diberikan data pebalap motogp sebagai berikut:

Nomor | Nama | Motor
----- | ---- | -----
46 | Rossi | Yamaha
93 | Marquez | Honda
04 | Dovizioso | Ducati
45 | Rins | Suzuki
55 | Syahrin | KTM

kita akan coba membuat database MySQL dari data diatas

1. Membuat Database
   ```
   import mysql.connector

    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb"
    )
   
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE motogp")
    ```
2. Membuat Table
3. Menambahkan Data
4. Menampilkan Data

```
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
```

hasilnya

```
(1, '46', 'Rossi', 'Yamaha')
(2, '93', 'Marquez', 'Honda')
(3, '04', 'Dovizioso', 'Ducati')
(4, '42', 'Rins', 'Suzuki')
(5, '55', 'Syahrin', 'KTM')
```
