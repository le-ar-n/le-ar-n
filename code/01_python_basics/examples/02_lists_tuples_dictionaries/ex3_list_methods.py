"""List methods"""

new_list = ["string", 5, 12.1, True, 16]

# Adding to list datatypes can be done in a few different ways
# Using the append command to add an item to the end of a list
new_list.append("new item appended")
print(new_list)
# Inserting an item at a specified index
new_list.insert(2, "This is the 2nd index")
print(new_list)
# Multiple list items can be added with extend, using a second list to extend the former
new_list.extend(["potato", "tomato", 24]) # note: this can be any iterable; list, tuple, dictionaries

# Items can also be removed from the list
# Removing an item of the list based on index
new_list.pop(2)
print(new_list)
# An item can also be deleted based on the value
new_list.remove("tomato")
print(new_list)

# Reversing a list¶
new_list.reverse()
print(new_list)

# Sorting
int_list = [6, 4, 2, 5, 7]
int_list.sort()
print(int_list)