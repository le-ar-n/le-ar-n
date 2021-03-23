"""While statement"""
# repeats statement for as long as the condition is TRUE 
condition = 0
while condition < 10:
    condition += 1
    print(condition)
else:
    print("while statement succesfully completed")

# break statement can be used to exit the while statement without executing the else statement
condition = "line of characters"
i = 0
while True:
    if condition[i] == "a":
        print("Found an 'a'")
        break
    elif len(condition)-1 == i:
        print("No characters left...")
        break
    i += 1