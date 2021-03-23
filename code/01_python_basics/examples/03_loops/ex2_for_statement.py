"""For statement"""
# iterating over number range
for i in range(5):
    print(n / 5.0 + 100)

# iterating over a sequence of items (usually a list)
pets = ["dog", "cat", "horse", "rabbit", "snake"]
for pet in pets:
    print(pet)

# iterating over string
for letter in "Python":
    print("current letter: ", letter)

# index and items in list
for i, pet in enumerate(pets):
    if pet == "dog":
        print("Found a dog at index: ", i)
    else:
        print("Not a dog")

# iterating over two lists (with the same length)
homes = ["house", "flat", "farm", "office", "basement"]
for pet, home in zip(pets, homes):
    print("The {} lives in the {}".format(pet, house))