# Import statistics module
import statistics

# Define a list of numbers
numbers = [1, 4, 17, 62, 12, 84, 5, 8, 21]

# Calculate mean
mean = statistics.mean(numbers)

# Calculate median
median = statistics.median(numbers)

# Calculate mode
mode = statistics.mode(numbers)

# Calculate standard deviation
stdev = statistics.stdev(numbers)

# Print the results
print("Mean: {:f}".format(mean))
print("Median: {:f}".format(median))
print("Mode: {:f}".format(mode))
print("Standard Deviation: {:f}".format(stdev))
