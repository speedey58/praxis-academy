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
2. Membuat Table
3. Menambahkan Data
4. Menampilkan Data
