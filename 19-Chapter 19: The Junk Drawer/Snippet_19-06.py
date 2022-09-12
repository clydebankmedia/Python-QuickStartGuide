# Import threading, datetime, and time modules
import threading
import datetime
import time

# Define the function for threading
def thread_loop(name):
    # Loop 10 times
    for i in range(10):
        # Get a string with the current time in ISO 8601 format
        now = datetime.datetime.now().isoformat()
        # Display the time
        print(name + " - current time: " + now)
        # Sleep 1 second
        time.sleep(1)

# Create several threads
thread1 = threading.Thread(target = thread_loop, args = ("thread1", ))
thread2 = threading.Thread(target = thread_loop, args = ("thread2", ))
thread3 = threading.Thread(target = thread_loop, args = ("thread3", ))

# Start each thread
thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish before exiting
thread3.join()
thread2.join()
thread1.join()
