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

akan dibuat tabel MySQL beserta relasinya di cockroachdb
```
root@127.133.241.80:34887/movr> CREATE TABLE gelar (
salutation_id INT PRIMARY KEY NOT NULL,
salutation STRING
);
CREATE TABLE

Time: 3.937694ms

root@127.133.241.80:34887/movr> CREATE TABLE nama (
membership_id INT PRIMARY KEY NOT NULL,
full_names STRING,
physical_address STRING,
salutation_id INT REFERENCES gelar(salutation_id) ON UPDATE NO ACTION
);
CREATE TABLE

Time: 39.420427ms

root@127.133.241.80:34887/movr> CREATE TABLE film (
membership_id INT REFERENCES nama(membership_id) ON UPDATE NO ACTION,
movies_rented STRING
);
CREATE TABLE

Time: 17.145604ms

root@127.133.241.80:34887/movr> show table;
invalid syntax: statement ignored: at or near "table": syntax error
DETAIL: source SQL:
show table
     ^
HINT: try \h SHOW
root@127.133.241.80:34887/movr> show tables;
          table_name          
+----------------------------+
  film                        
  gelar                       
  movies                      
  nama                        
  profil                      
  profile                     
  promo_codes                 
  rides                       
  salutation                  
  user_promo_codes            
  users                       
  vehicle_location_histories  
  vehicles                    
(13 rows)

Time: 1.546541ms

root@127.133.241.80:34887/movr> INSERT INTO gelar (salutation_id,salutation) VALUES
(1,'Mr.'),
(2,'Ms.'),
(3,'Mrs.'),
(4,'Dr.');
INSERT 4

Time: 2.170094ms

root@127.133.241.80:34887/movr> INSERT INTO nama (membership_id,full_names,physical_address,salutation_id) VALUES
                             -> (1,'janet_jones','first_street_plot4',2),
                             -> (2,'robert_phil','3rd_street_34',1),
                             -> (3,'robert_phil','5th_avenue',1);
INSERT 3

Time: 2.476636ms

root@127.133.241.80:34887/movr> INSERT INTO film (membership_id,movies_rented) VALUES
                             -> (1,'pirates_of_the_caribbean'),
                             -> (1,'clash_of_the_titans'),
                             -> (2,'forgetting_sarah_marshal'),
                             -> (2,'daddys_little)girl'),
                             -> (3,'clash_of_the_titans');
INSERT 5

Time: 2.659049ms
```
tampilkan data
```
root@127.133.241.80:34887/movr> SELECT * FROM nama;
  membership_id | full_names  |  physical_address  | salutation_id  
+---------------+-------------+--------------------+---------------+
              1 | janet_jones | first_street_plot4 |             2  
              2 | robert_phil | 3rd_street_34      |             1  
              3 | robert_phil | 5th_avenue         |             1  
(3 rows)

Time: 833.809µs

root@127.133.241.80:34887/movr> SELECT * FROM gelar;
  salutation_id | salutation  
+---------------+------------+
              1 | Mr.         
              2 | Ms.         
              3 | Mrs.        
              4 | Dr.         
(4 rows)

Time: 573.355µs

root@127.133.241.80:34887/movr> SELECT * FROM film;
  membership_id |      movies_rented        
+---------------+--------------------------+
              1 | pirates_of_the_caribbean  
              1 | clash_of_the_titans       
              2 | forgetting_sarah_marshal  
              2 | daddys_little)girl        
              3 | clash_of_the_titans       
(5 rows)

Time: 570.615µs

root@127.133.241.80:34887/movr> 
```
dengan menggunakan python, akan ditampilkan film apa saja yang ditonton Janet Jones
