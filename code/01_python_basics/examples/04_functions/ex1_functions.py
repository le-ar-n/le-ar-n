"""Functions"""
# Functions are blocks of code that can be used multiple times

def my_func():
    print("this is my first function")

my_func()

# add
def my_func_add(a, b):
    c = a + b
    return c
    
new_var = my_func_add(3,7)
print(new_var)

#  nested functions
def my_second_func(a, b):
    c = 4 * my_func_add(a, b)
    return c

a = 3
b = 10

result = my_second_func(a, b)
print(result)