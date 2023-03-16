# Import the hashlib module
import hashlib

# Define two sets of data
original_data = "The quick brown fox jumped over the lazy red dog."
new_data = "The quick brown fox leaped over the spry orange cat."

# Hash them both
original_hash = hashlib.sha256(original_data.encode()).hexdigest()
new_hash = hashlib.sha256(new_data.encode()).hexdigest()

# Display the results
print("Original SHA256 hash: " + original_hash)
print("New SHA256 hash: " + new_hash)
