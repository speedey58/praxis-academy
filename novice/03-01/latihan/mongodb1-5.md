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
Diberikan data keluarga sbb

nomer | nama | status | usia
------|------|--------|------
1 | Erfan Kurniawan | ayah | 34
2 | Shinta Devianti | bunda | 33
3 | Aghnia C Kurniawan | kakak | 5
4 | R Alghozi Kurniawan | adek | 2

selanjutnya akan dibuat data seperti di atas menggunakan mongodb, untuk mulai menggunakan server ketikkan pada terminal sbb: 

```
(base) minion@minion-PC:~$ sudo service mongodb start
(base) minion@minion-PC:~$ mongo
MongoDB shell version: 3.2.11
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
	http://docs.mongodb.org/
Questions? Try the support group
	http://groups.google.com/group/mongodb-user
```
* Create

  akan dibuat database keluarga dengan data sesuai tabel diatas
  ```
  > db.keluarga.insert({
  ... nomer:1,
  ... nama:"Erfan Kurniawan",
  ... status:"ayah",
  ... usia:34
  ... })
  WriteResult({ "nInserted" : 1 })
  > db.keluarga.insert({
  ... nomer:2,
  ... nama:"Shinta Devianti",
  ... status:"bunda",
  ... usia:33
  ... })
  WriteResult({ "nInserted" : 1 })
  > db.keluarga.insert({
  ... nomer:3,
  ... nama:"Aghnia C Kurniawan",
  ... status:"kakak",
  ... usia:5
  ... })
  WriteResult({ "nInserted" : 1 })
  > db.keluarga.insert({
  ... nomer:4,
  ... nama:"R Alghozi Kurniawan",
  ... status:"adek",
  ... usia:2
  ... })
  WriteResult({ "nInserted" : 1 })
  ```
  untuk mengecek jumlah entry yg telah dibuat
  ```
  > db.keluarga.count()
  4
  ```
* Read

  untuk menampilkan isi data seluruhnya
  ```
  > db.keluarga.find().pretty()
  {
   "_id" : ObjectId("5e703fb177e9557cf895d191"),
   "nomer" : 1,
   "nama" : "Erfan Kurniawan",
   "status" : "ayah",
   "usia" : 34
  }
  {
   "_id" : ObjectId("5e703ffd77e9557cf895d192"),
   "nomer" : 2,
   "nama" : "Shinta Devianti",
   "status" : "bunda",
   "usia" : 33
  }
  {
   "_id" : ObjectId("5e70404277e9557cf895d193"),
   "nomer" : 3,
   "nama" : "Aghnia C Kurniawan",
   "status" : "kakak",
   "usia" : 5
  }
  {
   "_id" : ObjectId("5e70407777e9557cf895d194"),
   "nomer" : 4,
   "nama" : "R Alghozi Kurniawan",
   "status" : "adek",
   "usia" : 2
  }
  ```
  untuk menampilkan isi data tertentu, dalam hal ini akan ditampilkan data yang berusia:5
  ```
  > db.keluarga.find({usia:5}).pretty()
  {
   "_id" : ObjectId("5e70404277e9557cf895d193"),
   "nomer" : 3,
   "nama" : "Aghnia C Kurniawan",
   "status" : "kakak",
   "usia" : 5
  }
  ```
* Update

  Waktu berjalan, bunda shinta hamil anak ke3. sehingga status alghozi (nomer:4) akan berubah statusnya dari *adek* menjadi
  *kakak ke2*, untuk mengubahnya dengan syntax sbb:
  ```
  > db.keluarga.update(
  ... {nomer:4}
  ... ,
  ... {
  ... nomer:4,
  ... nama:"R Alghozi Kurniawan",
  ... status:"kakak ke2",
  ... usia:5
  ... }
  ... )
  ```
  tampilkan datanya
  ```
  > db.keluarga.find({nomer:4}).pretty()
  {
   "_id" : ObjectId("5e70407777e9557cf895d194"),
   "nomer" : 4,
   "nama" : "R Alghozi Kurniawan",
   "status" : "kakak ke2",
   "usia" : 5
  }
  ```
* Delete

  untuk menghapus tabel sbb
  ```
  db.keluarga.drop();
  ```
  untuk menghapus database sbb
  ```
  db.dropDatabase();
  ```
## Motor Tornado
ketik perintah berikut di code editor untuk menginstal pip motor tornado
```
$ pip install tornado motor
```
