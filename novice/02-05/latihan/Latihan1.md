Microsoft Windows [Version 10.0.18362.719]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\ThinkPad L450 i5>cd "C:\Program Files (x86)\MariaDB 10.4\bin"

C:\Program Files (x86)\MariaDB 10.4\bin>mysql -u root -p
Enter password:
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\Program Files (x86)\MariaDB 10.4\bin>mysql -u root -p
Enter password: **
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)

C:\Program Files (x86)\MariaDB 10.4\bin>NO
'NO' is not recognized as an internal or external command,
operable program or batch file.

C:\Program Files (x86)\MariaDB 10.4\bin>mysql -u root -p
Enter password: *******
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 10.4.12-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database keluarga;
Query OK, 1 row affected (0.003 sec)

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

MariaDB [(none)]> use keluarga
Database changed
MariaDB [keluarga]> create table buku (
    -> nama(15),
    -> jabatan(15),
    -> tempat lahir(15),
    -> usia(2)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '(15),
jabatan(15),
tempat lahir(15),
usia(2)
)' at line 2
MariaDB [keluarga]> use keluarga
Database changed
MariaDB [keluarga]> create table profil (
    -> nomer varchar(2),
    -> nama varchar(25),
    -> tempat lahir varchar(10),
    -> usia varchar(2),
    -> primary key(nomer)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'lahir varchar(10),
usia varchar(2),
primary key(nomer)
)' at line 4
MariaDB [keluarga]> use keluarga
Database changed
MariaDB [keluarga]> create table profil (
    -> nomer varchar(2),
    -> nama varchar(25),
    -> tempat_lahir varchar(10),
    -> usia varchar(2),
    -> primary key(nomer)
    -> );
Query OK, 0 rows affected (0.168 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('01','Erfan Kurniawan','Denpasar','34');
Query OK, 1 row affected (0.067 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('02','Shinta Devianti','Wonosobo','33');
Query OK, 1 row affected (0.008 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('03','Aghnia C Kurniawan','Magelang','5');
Query OK, 1 row affected (0.008 sec)

MariaDB [keluarga]> INSERT INTO profil VALUES ('04','R Alghoozi Kurniawan','Magelang','2')
    -> ;
Query OK, 1 row affected (0.008 sec)

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

MariaDB [keluarga]>