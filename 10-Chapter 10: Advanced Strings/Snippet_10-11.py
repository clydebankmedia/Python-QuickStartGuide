# Import the regular expression engine
import re

# Define our content
text = "Hello, World!"

# Is "Hello" in our string?
if re.search("hello", text, re.IGNORECASE):
    print("hello is in the string.")
else:
    print("hello isn't in the string.")
