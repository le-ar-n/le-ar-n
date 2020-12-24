string_list = ["hello", "goodbye", "no more ideas", "etc."]

print(string_list[0], ", string_list element 1")
print(string_list[1], ", string_list element 2")

print(string_list)
string_list[1] = "replacement"
print(string_list)

list_nested = [[0,1,2], [3,4,5], [6,7,8]]
list_nested[0][1] = 5
print(list_nested)

print(string_list[2:4])
print(string_list[1:3])
print(string_list[-1])
print(string_list[-3:])