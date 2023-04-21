# ClydeBank Coffee Shop Simulator 4000
# Copyright 2022 (C) ClydeBank Media, All Rights Reserved.

# Import all functions from the utility module
from utilities import *

# Import the game class from the coffee_shop_simulator module
from coffee_shop_simulator import CoffeeShopSimulator

# Print welcome message
welcome()

# Get name and store name
t_name = prompt("What is your name?", True)
t_shop_name = prompt("What do you want to name your coffee shop?", True)

# Create the game object
game = CoffeeShopSimulator(t_name, t_shop_name)

# Run the game
game.run()
