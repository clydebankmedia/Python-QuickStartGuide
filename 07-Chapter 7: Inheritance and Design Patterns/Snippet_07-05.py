class Furniture:
    pass

class Chair(Furniture):
    pass

class Stool(Chair):
    def __init__(self, number):
        self.number = number

# Create an empty list named bar
bar = []

# Add 8 Stools to the Bar
for i in range(8):
    bar.append(Stool(i))

print(bar[2].number)
