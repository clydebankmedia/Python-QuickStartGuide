# Import the regular expression engine
import re

# Define our content
text = "The quick gray fox jumped over the lazy dog!"

# Find 
match = re.search("(gray|grey)", text, re.IGNORECASE)

# Print the match
print(match.group(0))
