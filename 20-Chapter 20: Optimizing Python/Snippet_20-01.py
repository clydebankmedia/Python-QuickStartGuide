import cProfile
import math

def myfunction(x):

    a = math.cos(x)
    b = math.pi
    c = math.e
    print(abs(a + b / c))

cProfile.run("for i in range(50000): myfunction(i)")
