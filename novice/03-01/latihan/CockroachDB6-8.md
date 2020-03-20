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
* Read
* Update
* Delete
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

root@127.57.29.25:46519/movr> SELECT * FROM drivers WHERE id in ('70a3d70a-3d70-4400-8000-000000000016', 'b851eb85-1eb8-4000-8000-000000000024');
                   id                  |  city   | name |  dl  | address  
+--------------------------------------+---------+------+------+---------+
  70a3d70a-3d70-4400-8000-000000000016 | chicago | NULL | NULL | NULL     
  b851eb85-1eb8-4000-8000-000000000024 | seattle | NULL | NULL | NULL     
(2 rows)

Time: 1.697692ms

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

root@127.57.29.25:46519/movr> SELECT id, name FROM users WHERE city = 'chicago';
  id | name  
+----+------+
(0 rows)

Time: 1.255197ms

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

root@127.57.29.25:46519/movr> DELETE FROM promo_codes WHERE description = 'EXPIRED';
DELETE 669

Time: 16.147441ms

root@127.57.29.25:46519/movr> DROP TABLE drivers;
DROP TABLE

Time: 74.60163ms
```
