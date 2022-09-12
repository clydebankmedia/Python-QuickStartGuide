# Define the average function
def average(*numbers):
    sum = 0
    for n in numbers:
        # Add n to sum
        # (+= means add n to sum and store in sum)
        sum += n
    return sum / len(numbers)

# Use our newly minted function
print(average(10, 40, 80, 74, 16, 42, 12, 6))
