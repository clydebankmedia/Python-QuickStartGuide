import cProfile

def slow_func():
    for i in range(100000):
        # Avoid this
        a = 1
        b = 2
        c = 3
        d = 4

def fast_func():
    for i in range(100000):
        # Instead, do this
        a, b, c, d = 1, 2, 3, 4

print("**** SLOW FUNCTION ****")
cProfile.run("slow_func()")

print("**** FAST FUNCTION ****")
cProfile.run("fast_func()")
