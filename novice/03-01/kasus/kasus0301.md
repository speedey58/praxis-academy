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
dengan menggunakan python, akan ditampilkan film apa saja yang ditonton Janet Jones
