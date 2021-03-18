# Lists
# Datastructures such as lists can contain any of the previously described datatypes
integer_list = [1, 3, 4, 6, 8, 11, 13]
float_list = [0.1, 1.4, 7.3, 12.2, 20.0]
string_list = ["hello", "goodbye", "no more ideas", "etc."]
boolean_list = [True, False, True, True, False]

# They can be printed and their type can be shown
print(integer_list, type(integer_list))
# A new list can also be created using the type, note the double round brackets
new_list = list(("strings", 5, 6, 6.7, True, "etc."))

# These lists have a certain length based on the amount of items in the datatype
length_of_list = len(integer_list)
print(length_of_list)


