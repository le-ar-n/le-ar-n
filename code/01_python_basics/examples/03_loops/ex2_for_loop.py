# For loop

# iterating over items of a sequence (usually a list)
pets = ["dog", "cat", "horse", "rabbit", "snake"]
for pet in pets:
    print(pet)

# iterating over number range
numbers = range(5)
print(list(numbers))
for n in numbers:
    print(n / 5.0 + 100)

# iterating over string
for letter in "Python":
    print("current letter: ", letter)

# index in range
print(len(pets))
print(list(range(len(pets))))

for index in range(0,len(pets)):
    print(index, pets[index])

# index and objects in list
for p,x in enumerate(pets):
    print(p, x)