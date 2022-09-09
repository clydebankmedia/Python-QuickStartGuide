class Furniture:
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

class Surface:
    def __init__(self, flat):
        self.flat = flat

class Table(Furniture, Surface):
    def __init__(self, width=0, height=0, material="Wood", flat=True):
        Furniture.__init__(self, width, height, material)
        Surface.__init__(self, flat)
        self.legs = 4

a = Table()
print(vars(a))
