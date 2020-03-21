import psycopg2

conn = psycopg2.connect(database='movr', user='root', host='127.115.187.186', port=42879)

conn.set_session(autocommit=True)

cur = conn.cursor()

cur.execute("SELECT \
    film.movies_rented \
    FROM nama \
    INNER JOIN film ON nama.membership_id = film.membership_id \
    WHERE nama.full_names='janet_jones'")
rows = cur.fetchall()
print('Janet Jones rent:')
for row in rows:
    print([str(cell) for cell in row])


cur.close()
conn.close()