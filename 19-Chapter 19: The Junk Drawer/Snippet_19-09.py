# Import the csv module
import csv

# Generate the data
sales_data = [
    ['Month', 'Coffee', 'Tea', 'Hot Chocolate', 'Espresso'],
    ['Jan', '523', '301', '507', '332'],
    ['Feb', '621', '339', '501', '339'],
    ['Mar', '512', '218', '497', '401'],
    ['Apr', '511', '401', '324', '385']
]

with open("sales-write.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in sales_data:
        writer.writerow(row)
