# Import the regular expression engine
import re

# Define our content
text = "The quick gray fox jumped over the lazy dog!"

# Find 
match = re.search("(gray|grey)", text, re.IGNORECASE)

# Get start and end of match
match_start = match.span()[0]
match_end = match.span()[1]

# Replacement text
replace_text = "grey"

# Replace gray with grey using the position from span
new_text = text[:match_start] + replace_text + text[match_end:]

# Display results
print("Old text: " + text)
print("New text: " + new_text)
