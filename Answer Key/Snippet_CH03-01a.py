from random import seed
from random import randint

number = randint(1, 10)

guess = int(input("Please pick a number between 1 and 10: "))

if guess == number:
	print("You guessed the number correctly!")
else:
	print("Sorry, that's incorrect. The number was " + str(number))
