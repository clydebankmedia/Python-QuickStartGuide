# Import the regular expression engine
import re

# Our string
test = "Hello, World!"

# Match
if re.match("e", test):
    print("re.match says it has an e in it.")

# Search
if re.search("e", test):
    print("re.search says it has an e in it.")
