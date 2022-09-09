# Import mysql-connector-python
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
	host = "localhost",
	user = "dbuser",
	password = "dbpass",
	database = "dbname"
)

# Grab a cursor object from the database connector
cursor = db.cursor()

# Run an SQL query to get all columns from the orders table
cursor.execute("SELECT * FROM orders")

# Return all results from the query
orders = cursor.fetchall()

# Step through orders and display order details
for order in orders:
  print(order)
