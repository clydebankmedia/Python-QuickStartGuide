# Load the zlib module
import zlib

# Define our data
data = """To compress data, we'll need a long string. 
Not a short string. No, that would be too small. 
To get any meaningful benefit from compression, 
you must use a decent length of data or else the
overhead of compression isn't worth the gains.
This will be enough data, containing enough redundant
patterns, to be compressible.""" 

# Compress the data
compressed_data = zlib.compress(data.encode())

# Display stats
data_len = len(data)
compressed_data_len = len(compressed_data)
print("Length of uncompressed data: " + str(data_len))
print("Length of compressed data: " + str(compressed_data_len))
