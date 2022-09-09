# Import the json module
import json

# Create a menu dictionary
menu = {"name": "Hot Chocolate", "price": 3.99}

# Convert to JSON
menu_json = json.dumps(menu)

# Display JSON
print(menu_json)
