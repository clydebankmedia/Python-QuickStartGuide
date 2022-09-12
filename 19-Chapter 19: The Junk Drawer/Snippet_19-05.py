# A simple customer list
customers = ["Robert", "Bryan", "John", "Jo", "Brittney"]

# Sort by last letter in name
customers.sort(key = lambda name: list(name)[-1])

# Display the results
print(customers)
