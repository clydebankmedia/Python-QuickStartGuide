import datetime

# The future date
future = datetime.datetime(2022, 10, 31, 0, 0)

# Now
now = datetime.datetime.now()

# Calculate difference
difference = future - now

# Display difference
print("It's " + str(difference) + " until " + str(future) + "!")
