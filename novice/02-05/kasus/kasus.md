Diberikan 3 tabel yang saling berelasi sbb:

Membership ID | Full Names | Physical Address | Salutation ID
--------------|------------|------------------|---------------
1 | Janet Jones | First Street Plot No.4 | 2
2 | Robert Phil | 3rd Street 34 | 1
3 | Robert Phil | 5th Avenue | 1

Membership ID | Movies Rented
--------------|--------------
1 | Pirates of the Caribbean
1 | Clash of the Titans
2 | Forgetting Sarah Marshal
2 | Daddy's Little Girls
3 | Clash of the Titans

Salutation ID | Salutation
--------------|-----------
1 | Mr.
2 | Ms.
3 | Mrs.
4 | Dr.

akan dibuat tabel MySQL beserta relasinya di Mariadb sbb

```
Microsoft Windows [Version 10.0.18362.720]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\ThinkPad L450 i5>cd "C:\Program Files (x86)\mariaDB 10.4\bin"

C:\Program Files (x86)\MariaDB 10.4\bin>mysql -u root -p
Enter password: *******
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 9
Server version: 10.4.12-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database kasus0205;
Query OK, 1 row affected (0.007 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| kasus0205          |
| keluarga           |
| motogp             |
| mysql              |
| performance_schema |
| test               |
+--------------------+
7 rows in set (0.022 sec)

MariaDB [(none)]> use kasus0205
Database changed

MariaDB [kasus0205]> create table salutation (
    -> salutation_id int PRIMARY KEY AUTO_INCREMENT,
    -> salutation varchar(5)
    -> );
Query OK, 0 rows affected (0.059 sec)

MariaDB [kasus0205]> create table namesaddress (
    -> membership_id int PRIMARY KEY AUTO_INCREMENT,
    -> full_names varchar(15),
    -> physical_address varchar(20),
    -> salutation_id int(2) NOT NULL,
    -> FOREIGN KEY (salutation_id) REFERENCES salutation(salutation_id)
    -> );
Query OK, 0 rows affected (0.033 sec)

MariaDB [kasus0205]> create table movie (
    -> membership_id int(2) NOT NULL,
    -> movie_rented varchar(30),
    -> FOREIGN KEY(membership_id) REFERENCES namesaddress(membership_id)
    -> );
Query OK, 0 rows affected (0.152 sec)

MariaDB [kasus0205]> INSERT INTO salutation VALUES
    -> (1,'Mr.'),
    -> (2,'Ms.'),
    -> (3,'Mrs.'),
    -> (4,'Dr.');
Query OK, 4 rows affected (0.082 sec)
Records: 4  Duplicates: 0  Warnings: 0

MariaDB [kasus0205]> SELECT * FROM salutation;
+---------------+------------+
| salutation_id | salutation |
+---------------+------------+
|             1 | Mr.        |
|             2 | Ms.        |
|             3 | Mrs.       |
|             4 | Dr.        |
+---------------+------------+
4 rows in set (0.007 sec)

MariaDB [kasus0205]> INSERT INTO namesaddress VALUES
    -> (1,'Janet_Jones','First_Street_Plot4',2),
    -> (2,'Robert_Phil','3rd_Street34',1),
    -> (3,'Robert_Phil','5th_Avenue',1);
Query OK, 3 rows affected (0.007 sec)
Records: 3  Duplicates: 0  Warnings: 0

MariaDB [kasus0205]> SELECT * FROM namesaddress;
+---------------+-------------+--------------------+---------------+
| membership_id | full_names  | physical_address   | salutation_id |
+---------------+-------------+--------------------+---------------+
|             1 | Janet_Jones | First_Street_Plot4 |             2 |
|             2 | Robert_Phil | 3rd_Street34       |             1 |
|             3 | Robert_Phil | 5th_Avenue         |             1 |
+---------------+-------------+--------------------+---------------+
3 rows in set (0.000 sec)

MariaDB [kasus0205]> INSERT INTO movie VALUES
    -> (1,'Pirates_of_the_Caribbean'),
    -> (1,'Clash_of_the_Titans'),
    -> (2,'Forgetting_Sarah_Marshal'),
    -> (2,'Daddys_Little_Girls'),
    -> (3,'Clash_of_the_Titans');
Query OK, 5 rows affected (0.015 sec)
Records: 5  Duplicates: 0  Warnings: 0

MariaDB [kasus0205]> SELECT * FROM movie;
+---------------+--------------------------+
| membership_id | movie_rented             |
+---------------+--------------------------+
|             1 | Pirates_of_the_Caribbean |
|             1 | Clash_of_the_Titans      |
|             2 | Forgetting_Sarah_Marshal |
|             2 | Daddys_Little_Girls      |
|             3 | Clash_of_the_Titans      |
+---------------+--------------------------+
5 rows in set (0.000 sec)
```
akan ditampilkan film apa saja yang dipinjam oleh Janet Jones, dengan menggunakan python sbb
```
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mariadb",
    database="kasus0205"
)

cursor = db.cursor()
sql = "SELECT \
    namesaddress.full_names, \
    movie.movie_rented \
    FROM namesaddress \
    INNER JOIN movie ON namesaddress.membership_id = movie.membership_id \
    WHERE namesaddress.full_names='Janet_Jones'"

cursor.execute(sql)
results = cursor.fetchall()

for data in results:
    print(data)
```
hasilnya
```
('Janet_Jones', 'Pirates_of_the_Caribbean')
('Janet_Jones', 'Clash_of_the_Titans')
```
