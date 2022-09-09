# Import the math module
import math

# Ask user for a number
number = input("Please enter a number: ")

# Convert to int
number = int(number)

# Calculate result
result = math.sqrt(number)

# Display result
print("The square root of {:n} is {:.6f}".format(number, result))
