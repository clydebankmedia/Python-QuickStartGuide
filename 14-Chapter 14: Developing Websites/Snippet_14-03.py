# Import mysql-connector-python
import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user = "dbuser",
	password = "dbpass",
	database = "dbname"
)
