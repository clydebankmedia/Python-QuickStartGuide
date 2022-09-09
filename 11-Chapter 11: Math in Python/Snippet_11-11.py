# Import datetime
import datetime

# Get the current time and date
now = datetime.datetime.now()

# Create a delta of 18 hours and 49 minutes
delta = datetime.timedelta(hours = 18, minutes = 49)

# Subtract delta and store in previous_time
previous_time = now - delta

# Display time and time minus the delta
print(now)
print(previous_time)
