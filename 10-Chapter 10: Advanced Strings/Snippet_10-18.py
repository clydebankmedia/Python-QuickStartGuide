# Import the regular expression engine
import re

# Our string
test = "The quick brown fox is fast!"

# Split by spaces using the \s metacharacter
# Since we want to account for multiple spaces, we add +
space_split = re.split("\s+", test)
print(space_split)

# Split by word using the non-word metacharacter
# Since we want to account for multiple
# non-word characters, we add +
word_split = re.split("\W+", test)
print(word_split)
