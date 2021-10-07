import mysql.connector

cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="scott",
  password="password",
  database="database"
)

cursor = cnx.cursor()

# sample query
query = ("insert into products(name, uom_id, price_per_unit) values('banana','1','40')")

cursor.execute(query)

# Make sure data is committed to the database
cnx.commit()

cnx.close()