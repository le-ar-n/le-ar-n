number_list = [1, 3, 4, 6, 8, 11, 13]
string_list = ["hello", "goodbye", "no more ideas", "etc."]
mixed_list = ["strings", 5, 6, 6.7, True, "etc."]

a = range(1,10)

print(list(a))
print(list(range(1,100,5)))
print(list(range(100, -10, -20)))

print(len(string_list))
print(string_list + number_list)
print(string_list*3)
print("hello" in string_list)
print("houdini" in string_list)

