# Import sys module
import sys

# Read stdin into data_in
data_in = sys.stdin.read()

# Write to stdout
bytes_written = sys.stdout.write(data_in)

# Display stats
print("Wrote {} bytes to stdout.".format(bytes_written))
