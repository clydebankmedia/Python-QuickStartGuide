# Import the regular expression engine
import re

# Our string
test = "The quick brown fox is fast!"

# Substitute spaces for +
plus_test = re.sub("\s+", "+", test)
print(plus_test)
