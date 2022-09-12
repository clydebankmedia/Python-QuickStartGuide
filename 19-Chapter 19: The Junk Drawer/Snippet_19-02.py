# Import pretty print
import pprint

# Create a menu dictionary
menu = [
    {"name": "Hot Chocolate", "price": 3.99},
    {"name": "Coffee", "price": 3.50},
    {"name": "Tea", "price": 2.99},
    {"name": "Orange Juice", "price": 1.99},
    {"name": "Soda", "price": 1.75},
]

# Create sort function


def sort_by(s):
    return s["name"]


# Sort by function
menu.sort(key=sort_by)

# Display results
pprint.pprint(menu)
