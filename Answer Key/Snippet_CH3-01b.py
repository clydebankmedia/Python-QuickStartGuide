from random import seed
from random import randint

number = randint(1, 10)

guess = int(input("Please pick a number between 1 and 10: "))

while guess != number:
    guess = int(input("Sorry, that's incorrect. Try again: "))

print("You guessed the number correctly!")
