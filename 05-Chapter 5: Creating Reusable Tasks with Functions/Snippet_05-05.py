def full_name(first="First", middle="Middle", last="Last", display=False):
    name = first + " " + middle + " " + last
    if display:
        print(name)
    return name

a = full_name()
print(a)
