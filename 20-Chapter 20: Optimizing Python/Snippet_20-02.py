def percent(n):
    return (str(n * 100) + "%")

def long_task():
    # Start a long loop and do some string work
    for i in range(100000):
        a = "Hello, World!"
        b = a + " " + a
        c = len(b)
        for j in range(c):
            d = b[j]
            e = d
        progress = i / 100000
        print(percent(progress))

long_task()
