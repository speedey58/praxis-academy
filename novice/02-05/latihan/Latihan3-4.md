### Instalasi Mariadb Connector
Install MariaDB connector menggunakan pip sebagai berikut:
```
pip3 install mysql-connector
```
tunggu hingga proses download selesai

### Koneksi ke MySQL dari python
buat file baru #connect.py# sebagai berikut
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
host diisikan "localhost", user diisikan "root", passwd diisikan pasword untuk mengakses database. Jalankan file python di atas, jika koneksi sukses akan muncul #Berhasil terhubung ke database#.

### Membuat database dari python 