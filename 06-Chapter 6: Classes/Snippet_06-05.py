# This variable exists in the main scope
name = "Sarah"

# Define a new class with a class variable called name
class Customer:
	def __init__(self, name):
		self.name = name

# Create a new customer so that __init__ is called
customer = Customer("Robert")

# Display the name in the main scope
print(customer.name)
