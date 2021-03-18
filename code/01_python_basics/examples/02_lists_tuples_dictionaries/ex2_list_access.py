# Lists are indexed and items can be obtained based on the index
integer_list = [1, 3, 4, 6, 8, 11, 13]
float_list = [0.1, 1.4, 7.3, 12.2, 20.0]
string_list = ["hello", "goodbye", "no more ideas", "etc."]
boolean_list = [True, False, True, True, False]
new_list = list(("strings", 5, 6, 6.7, True, "etc."))

# The index starts at 0 and continues to the list length - 1 -> [0...n] where n = len(list)-1
print("This is item at index 0: ", integer_list[0])
print("This is item at index 3: ", string_list[3])

# Indexes also can be negative, taking from the last items in the list [-n...0] where n = len(list)-1
print("This is item at index -1: ", float_list[-1])
print("This is item at index -4: ", boolean_list[-4])

# Ranges can be defined which return a selection of indexes
print("This returns the 1st until the 4th index: ", new_list[1:5]) # notice the last index (5) is not included while the first (1) is included -> [1,2,3,4]
print("This returns all before the 3rd index: ", new_list[:4]) # notice the last index (4) is again not included -> [0,1,2,3]
print("This returns all after the 2nd index: ", new_list[2:]) # notice the first index (2) IS included -> [2,3,4]

# These indexes can also be used to replace items
new_list[0] = "replacement_string"
print(new_list)
# This can also be done using range of indexes
new_list[1:3] = [100, 16.6] 
print(new_list)
# lists can also contain lists (called nested lists)
new_list[4] = ["list", "inside", "list"] 
print(new_list