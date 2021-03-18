# A tuple is similar to a list, however the sequence is immutable.
# This means, they can not be changed or added to.

my_tuple_1 = (1, 2, 3)

print(my_tuple_1, type(my_tuple_1))
print(len(my_tuple_1))

my_tuple_2 = tuple(("hello", "goodbye"))

print(my_tuple_2[0])
print(my_tuple_2[-1])
print(my_tuple_2[1:3])