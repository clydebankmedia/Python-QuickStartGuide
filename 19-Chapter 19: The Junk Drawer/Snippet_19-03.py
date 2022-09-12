# Import the os module
import os

# Iterate over environment variables and display the variable and its value
for k, v in os.environ.items():
	print(k + " = " + v)
