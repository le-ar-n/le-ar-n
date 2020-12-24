# Initializing empty list
my_list = []

# Appending single objects to a list
my_list.append(1)
print(my_list)
my_list.append(10)
print(my_list)
my_list.append(100)
print(my_list)

# Extending a list with lists
my_list.extend([5]*10)
print(my_list)

# Inserting an object into a list at specific index
my_list.insert(0, "start")
print(my_list)
my_list.insert(len(my_list), "end")
print(my_list)

# Removing and returning objects from a list
obj = my_list.pop()
print(my_list)
print(obj)

my_list.remove(10)
print(my_list)

# Reversing a list¶
my_list.reverse()
print(my_list)

# Sorting
my_list.sort()
print(my_list)