# Import the sqlite3 module
import sqlite3

# Create a db object by connecting to the sTunes.db database
db = sqlite3.connect("sTunes.db")

# Run a SELECT query, then loop through
# the results and display the row data

query = "select * from tracks"

for row in db.execute(query):
	print(row)
