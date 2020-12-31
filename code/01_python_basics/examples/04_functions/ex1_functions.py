"""
we use functions for actions that we repeat multiple times
"""

def my_func():
    print("this is my first function")

my_func()

# add
def my_func_add(a, b):
    c = a + b
    print(c)

my_func_add(3,7)

# return
def my_func_add(a, b):
    c = a + b
    if c == 10:
        return True
    else:
        return False

my_var = my_func_add(3, 7)
print(my_var)

#  nested functions
def my_second_func(a, b):
    c = 4 * my_func_add(a, b)
    return c

nb_1 = 3
nb_2 = 10

result = my_second_func(nb_1, nb_2)
print(result)

