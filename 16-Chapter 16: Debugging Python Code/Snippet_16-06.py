# Import the time module so we can use sleep
import time

running = True
a = 0

while running:
    print("Hello, World!")
    print("a is " + str(a))
    a += 1

    # Pause execution for 1 second
    time.sleep(1)
