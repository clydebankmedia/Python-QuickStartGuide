# Divide a number by zero
a = 7
b = 0

try:
    print(str(a) + " divided by " + str(b) + " is " + str(a / b))
except Exception as e:
    print("Sorry, a problem occurred dividing the numbers.")
    print("Error details: " + str(e))

print("All done!")
