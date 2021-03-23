"""Dictionary datatype"""

# Unordered datatype with key:value pairs, there are no duplicates allowed
my_dict = {
    "name" : "Kathrin", 
    "age" : 71, 
    "profession" : "Still not decided"
}

print(len(my_dict))
print(type(my_dict))
print("These are keys: ", my_dict.keys())
print("These are the values: ", my_dict.values())
print("These are key:value pairs: ", my_dict.items())

# Values can be called using the key
print("my_dict['name']: ", my_dict['name'])
print("my_dict['age']: ", my_dict['age'])

# Values can be updated
my_dict['age'] = 25
print("my_dict['age']: ", my_dict['age'])

# New key:value pairs can be added and updated
my_dict['chair'] = "Digital Fabrication"
my_dict.update({"height":166, "profession":"Nerd"})

# Items can also be removed from the dictionary
my_dict.pop("height")
print(my_dict)

# The dictionary can also be cleared
my_dict.clear()
print(my_dict)