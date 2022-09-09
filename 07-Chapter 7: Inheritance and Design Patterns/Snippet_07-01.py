# First, let's define the Furniture class
class Furniture:
    def __init__(self, width=0, height=0, material="Wood"):
        self.width = width
        self.height = height
        self.material = material

# Next, let's define the Chair class
class Chair(Furniture):
    def __init__(self, width=0, height=0, material="Wood", arms=True, back=True):
        super().__init__(width, height, material)
        self.arms = arms
        self.back = back

    def fold(self):
        self.folded = True
        print("The chair is now folded and ready for transport.")

    def unfold(self):
        self.folded = False
        print("The chair is now unfolded and ready for use.")
