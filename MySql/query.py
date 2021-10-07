import mysql.connector

cnx = mysql.connector.connect(
  host="127.0.0.1",
  user="scott",
  password="password",
  database="database"
)

cursor = cnx.cursor()

# sample query
query = "SELECT * FROM gs.products"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()