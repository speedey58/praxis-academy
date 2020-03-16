## Instalasi Mongodb di Linux
 ketikkan perintah berikut di terminal
 ```
 sudo apt install mongdb
 ```
 tunggu sampai proses instalasi selesai

## Mongo Shell Manual

* Menyalakan server MongoDB:
  ```
  sudo service mongodb start
  ```
* Mematikan server MongoDB:
  ```
  sudo service mongodb stop
  ```
* Menyalakan ulang server MongoDB:
  ```
  sudo service mongodb restart
  ```
* Melihat status server MongoDB:
  ```
  sudo service mongodb status
  ```
* Mengakses server mongodb
  ```
  mongo
  ```
* Membuat database dan koleksi baru
  ```
  db.createCollections("nama_koleksi")
  ```
* Insert data
  ```
  db.<koleksi>.insert(<data>)
  ```
* Menampilkan data
  ```
  db.<koleksi>.find()
  ```
* Mengubah data
  ```
  db.<koleksi>.update(<query>, <data baru>)
  ```
* Menghapus data
  ```
  db.<koleksi>.remove(<query>)
  ```
* Menghapus koleksi:
  ```
  db.<koleksi>.drop();
  ```
* Menghapus database:
  ```
  db.dropDatabase();
  ```
## MongoDB CRUD
* Create
* Read
* Update
* Delete

## Motor Tornado
ketik perintah berikut di code editor untuk menginstal pip motor tornado
```
$ pip install tornado motor
```
