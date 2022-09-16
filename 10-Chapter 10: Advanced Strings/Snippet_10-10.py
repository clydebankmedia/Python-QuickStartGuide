# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Is "Hello" in our string?
if re.search("Hello", text):
    print("Hello is in the string.")
else:
    print("Hello isn't in the string.")
