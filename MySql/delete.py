import mysql.connector

cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="scott",
  password="password",
  database="database"
)

cursor = cnx.cursor()

# sample query
query = ("delete from products where product_id=26")

cursor.execute(query)

cnx.commit()

cnx.close()