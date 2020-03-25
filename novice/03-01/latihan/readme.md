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


## Instalasi CockroachDB
copy dan ketikkan di terminal untuk mendownload cockroachdb
```
wget -qO- https://binaries.cockroachdb.com/cockroach-v19.2.4.linux-amd64.tgz | tar  xvz
```
untuk memudahkan mengeksekusi cockroachdb copy binary ke dalam path dengan menjalankan perintah berikut diterminal
```
cp -i cockroach-v19.2.4.linux-amd64/cockroach /usr/local/bin/
```

## CRUD CockroachDB

ketikkan perintah berikut di terminal untuk memulai sesi demo cockroach
```
(base) minion@minion-PC:~$ cockroach demo
```
akan muncul sbb:
```
#
# Welcome to the CockroachDB demo database!
#
# You are connected to a temporary, in-memory CockroachDB cluster of 1 node.
#
# This demo session will attempt to enable enterprise features
# by acquiring a temporary license from Cockroach Labs in the background.
# To disable this behavior, set the environment variable
# COCKROACH_SKIP_ENABLING_DIAGNOSTIC_REPORTING=true.
#
# The cluster has been preloaded with the "movr" dataset
# (MovR is a fictional vehicle sharing company).
#
# Reminder: your changes to data stored in the demo session will not be saved!
#
# Web UI: http://127.57.29.25:35781
#
# Server version: CockroachDB CCL v19.2.4 (x86_64-unknown-linux-gnu, built 2020/02/06 21:55:19, go1.12.12) (same version as client)
# Cluster ID: d8f23c79-0261-43e5-8cae-096d27423190
#
# Enter \? for a brief introduction.
#
```
ketikkan *show tables* untuk melihat tabel didalam database
```
root@127.57.29.25:46519/movr> show tables
                           -> ;
          table_name          
+----------------------------+
  promo_codes                 
  rides                       
  user_promo_codes            
  users                       
  vehicle_location_histories  
  vehicles                    
(6 rows)

Time: 3.306837ms
```
dari hasil yang keluar di atas, diketahui ada 6 tabel didalam database demo

* Create

  akan dibuat tabel __drivers__
  
    ```
    root@127.57.29.25:46519/movr> CREATE TABLE drivers (
        id UUID NOT NULL,
        city STRING NOT NULL,
        name STRING,
        dl STRING UNIQUE,
        address STRING,
        CONSTRAINT "primary" PRIMARY KEY (city ASC, id ASC)
    );
    CREATE TABLE

    Time: 6.998481ms

    root@127.57.29.25:46519/movr> CREATE TABLE IF NOT EXISTS drivers (
        id UUID NOT NULL,
        city STRING NOT NULL,
        name STRING,
        dl STRING UNIQUE,
        address STRING,
        CONSTRAINT "primary" PRIMARY KEY (city ASC, id ASC)
    );
    CREATE TABLE

    Time: 844.968µs
    ```
* Read

  untuk menampilkan database yang telah dibuat sbb:
  ```
  root@127.57.29.25:46519/movr> SHOW COLUMNS FROM drivers;
    column_name | data_type | is_nullable | column_default | generation_expression |         indices          | is_hidden  
  +-------------+-----------+-------------+----------------+-----------------------+--------------------------+-----------+
    id          | UUID      |    false    | NULL           |                       | {primary,drivers_dl_key} |   false    
    city        | STRING    |    false    | NULL           |                       | {primary,drivers_dl_key} |   false    
    name        | STRING    |    true     | NULL           |                       | {}                       |   false    
    dl          | STRING    |    true     | NULL           |                       | {drivers_dl_key}         |   false    
    address     | STRING    |    true     | NULL           |                       | {}                       |   false    
  (5 rows)

  Time: 13.517637ms

  root@127.57.29.25:46519/movr> INSERT INTO drivers VALUES
      ('c28f5c28-f5c2-4000-8000-000000000026', 'new york', 'Petee', 'ABC-1234', '101 5th Ave');
  INSERT 1

  Time: 8.678797ms

  ```
* Update

  untuk mengisi data pada tabel yang telah dibuat sbb
  ```
  
  root@127.57.29.25:46519/movr> INSERT INTO drivers (name, city, dl, address, id) VALUES
      ('Adam Driver', 'chicago', 'DEF-5678', '201 E Randolph St', '1eb851eb-851e-4800-8000-000000000006');
  INSERT 1

  Time: 1.523111ms

  root@127.57.29.25:46519/movr> INSERT INTO drivers VALUES
      ('8a3d70a3-d70a-4000-8000-00000000001b', 'seattle', 'Eric', 'GHI-9123', '400 Broad St'),
      ('9eb851eb-851e-4800-8000-00000000001f', 'new york', 'Harry Potter', 'JKL-456', '214 W 43rd St');
  INSERT 2

  Time: 1.700985ms

  root@127.57.29.25:46519/movr> INSERT INTO drivers (id, city) VALUES
      ('70a3d70a-3d70-4400-8000-000000000016', 'chicago');
  INSERT 1

  Time: 2.219211ms

  root@127.57.29.25:46519/movr> INSERT INTO drivers (id, city, name, dl, address) VALUES
      ('b851eb85-1eb8-4000-8000-000000000024', 'seattle', DEFAULT, DEFAULT, DEFAULT);
  INSERT 1

  Time: 2.197869ms
  ```
  akan ditampilkan data tertentu yang sudah diinput
  ```
  root@127.57.29.25:46519/movr> SELECT * FROM drivers WHERE id in ('70a3d70a-3d70-4400-8000-000000000016', 'b851eb85-1eb8-4000-8000-000000000024');
                     id                  |  city   | name |  dl  | address  
  +--------------------------------------+---------+------+------+---------+
    70a3d70a-3d70-4400-8000-000000000016 | chicago | NULL | NULL | NULL     
    b851eb85-1eb8-4000-8000-000000000024 | seattle | NULL | NULL | NULL     
  (2 rows)

  Time: 1.697692ms
  ```
  membuat index sbb:
  ```
  root@127.57.29.25:46519/movr> CREATE INDEX name_idx ON users (name DESC);
  CREATE INDEX

  Time: 107.087545ms

  root@127.57.29.25:46519/movr> CREATE TABLE IF NOT EXISTS drivers (
      id UUID NOT NULL,
      city STRING NOT NULL,
      name STRING,
      dl STRING,
      address STRING,
      INDEX name_idx (name),
      CONSTRAINT "primary" PRIMARY KEY (city ASC, id ASC)
  );
  CREATE TABLE

  Time: 798.581µs
  ```
  menampilkan index yang telah dibuat
  ```
  root@127.57.29.25:46519/movr> SHOW INDEX FROM users;
    table_name | index_name | non_unique | seq_in_index | column_name | direction | storing | implicit  
  +------------+------------+------------+--------------+-------------+-----------+---------+----------+
    users      | primary    |   false    |            1 | city        | ASC       |  false  |  false    
    users      | primary    |   false    |            2 | id          | ASC       |  false  |  false    
    users      | name_idx   |    true    |            1 | name        | DESC      |  false  |  false    
    users      | name_idx   |    true    |            2 | city        | ASC       |  false  |   true    
    users      | name_idx   |    true    |            3 | id          | ASC       |  false  |   true    
  (5 rows)

  Time: 3.382278ms
  ```
  menampilkan data dengan kriteria tertentu
  ```
  root@127.57.29.25:46519/movr> SELECT name FROM users LIMIT 10;
          name         
  +-------------------+
    William Wood       
    Victoria Jennings  
    Tyler Dalton       
    Tony Ortiz         
    Tina Miller        
    Taylor Cunningham  
    Susan Morse        
    Steven Lara        
    Stephen Diaz       
    Sarah Wang DDS     
  (10 rows)

  Time: 1.033892ms

  root@127.57.29.25:46519/movr> SELECT * FROM users LIMIT 10;
                     id                  |   city    |        name         |            address            | credit_card  
  +--------------------------------------+-----------+---------------------+-------------------------------+-------------+
    ae147ae1-47ae-4800-8000-000000000022 | amsterdam | Tyler Dalton        | 88194 Angela Gardens Suite 94 | 4443538758   
    b3333333-3333-4000-8000-000000000023 | amsterdam | Dillon Martin       | 29590 Butler Plain Apt. 25    | 3750897994   
    b851eb85-1eb8-4000-8000-000000000024 | amsterdam | Deborah Carson      | 32768 Eric Divide Suite 88    | 8107478823   
    bd70a3d7-0a3d-4000-8000-000000000025 | amsterdam | David Stanton       | 80015 Mark Views Suite 96     | 3471210499   
    c28f5c28-f5c2-4000-8000-000000000026 | amsterdam | Maria Weber         | 14729 Karen Radial            | 5844236997   
    1eb851eb-851e-4800-8000-000000000006 | boston    | Brian Campbell      | 92025 Yang Village            | 9016427332   
    23d70a3d-70a3-4800-8000-000000000007 | boston    | Carl Mcguire        | 60124 Palmer Mews Apt. 49     | 4566257702   
    28f5c28f-5c28-4600-8000-000000000008 | boston    | Jennifer Sanders    | 19121 Padilla Brooks Apt. 12  | 1350968125   
    2e147ae1-47ae-4400-8000-000000000009 | boston    | Cindy Medina        | 31118 Allen Gateway Apt. 60   | 6464362441   
    33333333-3333-4400-8000-00000000000a | boston    | Daniel Hernandez MD | 51438 Janet Valleys           | 0904722368   
  (10 rows)

  Time: 1.78758ms

  root@127.57.29.25:46519/movr> SELECT id, name FROM users WHERE city = 'boston';
                     id                  |        name          
  +--------------------------------------+---------------------+
    1eb851eb-851e-4800-8000-000000000006 | Brian Campbell       
    23d70a3d-70a3-4800-8000-000000000007 | Carl Mcguire         
    28f5c28f-5c28-4600-8000-000000000008 | Jennifer Sanders     
    2e147ae1-47ae-4400-8000-000000000009 | Cindy Medina         
    33333333-3333-4400-8000-00000000000a | Daniel Hernandez MD  
    3851eb85-1eb8-4200-8000-00000000000b | Sarah Wang DDS       
  (6 rows)

  Time: 3.591458ms

  root@127.57.29.25:46519/movr> SELECT city, type, current_location FROM vehicles ORDER BY city, type DESC;
        city      |    type    |        current_location         
  +---------------+------------+--------------------------------+
    amsterdam     | scooter    | 57637 Mitchell Shoals Suite 59  
    amsterdam     | scooter    | 62609 Stephanie Route           
    boston        | scooter    | 19659 Christina Ville           
    boston        | scooter    | 47259 Natasha Cliffs            
    los angeles   | scooter    | 43051 Jonathan Fords Suite 36   
    new york      | skateboard | 64110 Richard Crescent          
    new york      | scooter    | 86667 Edwards Valley            
    paris         | skateboard | 2505 Harrison Parkway Apt. 89   
    paris         | skateboard | 19202 Edward Pass               
    rome          | bike       | 64935 Matthew Flats Suite 55    
    san francisco | skateboard | 49164 Anna Mission Apt. 38      
    san francisco | skateboard | 69721 Noah River                
    seattle       | skateboard | 81472 Morris Run                
    seattle       | scooter    | 91427 Steven Spurs Apt. 49      
    washington dc | bike       | 37754 Farmer Extension          
  (15 rows)

  Time: 4.701492ms
  ```
  update data dengan kriteria tertentu
  ```
  root@127.57.29.25:46519/movr> UPDATE promo_codes SET (description, rules) = ('EXPIRED', '{"type": "percent_discount", "value": "0%"}') WHERE expiration_time < '2019-01-22 03:04:05+00:00';
  UPDATE 669

  Time: 18.116115ms

  root@127.57.29.25:46519/movr> SELECT code, description, rules FROM promo_codes LIMIT 10;
              code            |                                                                                                   description                                                                                                    |                    rules                      
  +---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
    a_blue_member             | Yard send you end kitchen. High politics only support certainly. Reflect these agree travel bag myself. Month data magazine its trade water reality.                                                             | {"type": "percent_discount", "value": "10%"}  
    a_down_man                | EXPIRED                                                                                                                                                                                                          | {"type": "percent_discount", "value": "0%"}   
    ability_until_student     | Set hot parent statement organization charge. Wide new bag easy note each trial. Act compare information marriage. Through they speech top.                                                                      | {"type": "percent_discount", "value": "10%"}  
    about_mission_pull        | Main serious education economy situation turn. Away senior realize evidence. Far himself against look. Husband skin pick within. Sense garden sister draw theory remain.                                         | {"type": "percent_discount", "value": "10%"}  
    about_stuff_city          | Skill sing rich glass store whatever teach.                                                                                                                                                                      | {"type": "percent_discount", "value": "10%"}  
    accept_gas_hundred        | Listen much get art popular.                                                                                                                                                                                     | {"type": "percent_discount", "value": "10%"}  
    accept_resource_something | EXPIRED                                                                                                                                                                                                          | {"type": "percent_discount", "value": "0%"}   
    according_share_door      | Region difference letter now huge next any. Nothing hotel gas election hospital hope give. Capital can address look. Window off beyond success couple PM as hair. Side who understand indeed future system vote. | {"type": "percent_discount", "value": "10%"}  
    account_interest_next     | EXPIRED                                                                                                                                                                                                          | {"type": "percent_discount", "value": "0%"}   
    act_even_camera           | EXPIRED                                                                                                                                                                                                          | {"type": "percent_discount", "value": "0%"}   
  (10 rows)

  Time: 1.572896ms
  ```
* Delete

  untuk menghapus sebagian data
  ```
  root@127.57.29.25:46519/movr> DELETE FROM promo_codes WHERE description = 'EXPIRED';
  DELETE 669

  Time: 16.147441ms
  ```
  menghapus seluruh data
  ```
  root@127.57.29.25:46519/movr> DROP TABLE drivers;
  DROP TABLE

  Time: 74.60163ms
  ```
  
ketikkan __\q__ untuk keluar sessi

## Membangun Aplikasi Python dengan Cockroachdb

untuk dapat menjalankan aplikasi python pada database newSQL, diperlukan postgreSQL yaitu sebuah sistem basis data. salah satu sistem basis data yang populer adalah psycopg2. Untuk inisialisasi psycopg2 di python, cukup ketikkan perintah berikut di terminal.
```
pip3 install psycopg2
```
