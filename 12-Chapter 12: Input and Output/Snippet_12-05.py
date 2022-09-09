# Import the pickle module
import pickle

# Our data
customer_names = ["Jim Smith", "Amber Dobson", "Al James"]

# Write to disk
with open("customers.dat", mode = "wb") as f:
	pickle.dump(customer_names, f)

# Load the data
with open("customers.dat", mode = "rb") as f:
	loaded_data = pickle.load(f)

print("Original data : " + str(customer_names))
print("Loaded data   : " + str(loaded_data))
