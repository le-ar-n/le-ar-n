"""Recursion"""
# Functions can be called inside of the same function
def fibonacci(sequence):
    if sequence < 0:
        print("Incorrect input")
    if sequence == 0:
        return 0
    elif sequence == 1:
        return 1
    else:
        return fibonacci(sequence-1) + fibonacci(sequence-2)

fib_seq = 10
for i in range(fib_seq):
    print(fibonacci(i)) 