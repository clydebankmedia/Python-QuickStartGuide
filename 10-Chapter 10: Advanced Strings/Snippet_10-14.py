# Import the regular expression engine
import re

# Define our content
text = "This is the the house. It has red red paint."

# Regular expression to find duplicate words
# Use prefix r before to treat as raw (unescaped) string
regex = r"\b(\w+)\s+\1\b"

# Find any duplicate words
matches = re.findall(regex, text, re.IGNORECASE)

# Print the duplicate words
for match in matches:
	print(match)
