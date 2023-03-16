
# Define the generator function
# with the start argument defaulting to 99
def bottles_song(start=99):
    # Set the initial number of bottles to the start argument
    bottles = start
    # Loop through until bottles are gone
    while bottles > 0:
        # Display the song
        print(str(bottles) + " bottles of beer on the wall. ")
        print(str(bottles) + " bottles of beer.")
        print("Take one down, pass it around, ")
        print(str(bottles) + " bottles of beer on the wall.")
        # Subtract a bottle
        bottles -= 1
        # Yield to the calling function
        yield
    # Pick back up here when we return
    return True

# Loop through the generator
for i in bottles_song():
    # Don't do anything as the generator does the printing
    pass
