# Define the function full_name
def full_name(first, middle, last, display):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

# Use our newly created function
full_name("Robert", "W", "Oliver", True)
complete_name = full_name("Robert", "W", "Oliver", False)
print(complete_name)
