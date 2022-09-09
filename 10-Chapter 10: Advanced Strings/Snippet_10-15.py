# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Does the string begin with the letter H?
if re.search("^H", text):
	print("The string begins with H.")
else:
	print("The string does not begin with H.")
