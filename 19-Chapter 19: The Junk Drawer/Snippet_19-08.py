# Import the csv module
import csv

# Import the pprint module
from pprint import pprint

# Create empty list
sales_data = []

with open("sales.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		sales_data.append(row)		
pprint(sales_data)
