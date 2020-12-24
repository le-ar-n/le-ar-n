my_dict = {"Name" : "Kathrin", "Age" : 71, "Profession" : "Still not decided"}
print("my_dict['Name']: ", my_dict['Name'])
print("my_dict['Age']: ", my_dict['Age'])

my_dict['Age'] = 25; # update existing entry
print("my_dict['Age']: ", my_dict['Age'])

my_dict['Chair'] = "Digital Fabrication"; # add new entry
my_dict.update({"Height":166, "Profession":"Nerd"}) # update existing entries

print(my_dict)

# nested dicts
my_dict = {2:["a", 34], 62:(8, 1, 89), "test":{1:3, 5:67, "a":"b"}}
print(my_dict[62])
print(my_dict["test"]["a"])

# keys must be immutable types (integers, floats, strings, tuples)
# values can be anything
all_keys = my_dict.keys()
print(all_keys)