import cProfile
import math
import contextlib

# Avoid this
def slow_func():
    for i in range(100000):
        with contextlib.redirect_stdout(None):
            print(math.sin(math.pi / 3))

# Instead, do this
def fast_func():
    a = math.sin(math.pi / 3)
    for i in range(100000):
        with contextlib.redirect_stdout(None):
            print(a)

print("**** SLOW FUNCTION ****")
cProfile.run("slow_func()")

print("**** FAST FUNCTION ****")
cProfile.run("fast_func()")
