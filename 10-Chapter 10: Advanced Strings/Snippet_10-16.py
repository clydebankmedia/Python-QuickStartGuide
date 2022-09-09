# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Does the string end in an exclamation point?
if re.search("\!$", text):
	print("The string ends with an exclamation point.")
else:
	print("The string doesn't end with an exclamation point.")
