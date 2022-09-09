# Import datetime
import datetime

# Get the current time and date
now = datetime.datetime.now()

# Display date and time in a custom format
print(now.strftime("%A, %B %d, %Y at %I:%M %p"))
