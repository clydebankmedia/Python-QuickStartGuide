class Furniture:
    def __init__(self, width=0, height=0, material="Wood"):
        self.width = width
        self.height = height
        self.material = material

class Chair(Furniture):
    def __init__(self, material, width=0, height=0, arms=True, back=True):
        super().__init__(width, height, material)
        self.arms = arms
        self.back = back

class Bench(Chair):
    pass

sofa = Bench("Metal")
print(vars(sofa))
