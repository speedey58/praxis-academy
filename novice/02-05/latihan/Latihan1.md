### Instalasi Mariadb di Windows 10
klik link berikut <https://downloads.mariadb.org/>

### Membuat database sederhana
buka command prompt
masuk ke directory dimana mariadb terinstall
```
C:\Users\ThinkPad L450 i5>cd "C:\Program Files (x86)\MariaDB 10.4\bin"
```
ketikkan perintah *mysql -u root -p* untuk memulai membuat database, masukkan pasword sesuai dengan pasword yang dibuat waktu pengistalan
```
C:\Program Files (x86)\MariaDB 10.4\bin>mysql -u root -p
Enter password: *******
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 10.4.12-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
```
buat nama database dengan perintah *create database [nama_database]*
```
MariaDB [(none)]> create database keluarga;
Query OK, 1 row affected (0.003 sec)
```
ketikkan *show databases*
```
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| keluarga           |
| mysql              |
| performance_schema |
| test               |
+--------------------+
5 rows in set (0.020 sec)
```
untuk mulai menggunakan database ketikkan *use [nama_database]*
```
MariaDB [(none)]> use keluarga
Database changed
```
untuk membuat nama tabel dan judul kolom perhatikan perintah berikut
```
MariaDB [keluarga]> create table profil (
    -> nomer varchar(2),
    -> nama varchar(25),
    -> tempat_lahir varchar(10),
    -> usia varchar(2),
    -> primary key(nomer)
    -> );
Query OK, 0 rows affected (0.168 sec)
```
untuk mengisi database ketikkan *INSERT INTO [nama_tabel] VALUES* kemudian diisikan masing-masing nilainya
```
MariaDB [keluarga]> INSERT INTO profil VALUES ('01','Erfan Kurniawan','Denpasar','34');
Query OK, 1 row affected (0.067 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('02','Shinta Devianti','Wonosobo','33');
Query OK, 1 row affected (0.008 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('03','Aghnia C Kurniawan','Magelang','5');
Query OK, 1 row affected (0.008 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('04','R Alghoozi Kurniawan','Magelang','2');

Query OK, 1 row affected (0.008 sec)
```
untuk menampilkan tabel yang telah dibuat
```
MariaDB [keluarga]> SELECT * FROM profil;
+-------+----------------------+--------------+------+
| nomer | nama                 | tempat_lahir | usia |
+-------+----------------------+--------------+------+
| 01    | Erfan Kurniawan      | Denpasar     | 34   |
| 02    | Shinta Devianti      | Wonosobo     | 33   |
| 03    | Aghnia C Kurniawan   | Magelang     | 5    |
| 04    | R Alghoozi Kurniawan | Magelang     | 2    |
+-------+----------------------+--------------+------+
4 rows in set (0.007 sec)
```
