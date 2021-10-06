"""Conditional statements"""

int_a = 57
var_2 = 74

if int_a == 57:
    print("The value of this variable is 57")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Using "else" to perform alternative action, for any value not caught by "if" statement
int_b = 100

if int_b == 57:
    print("The value of this variable is 57")
else:
    print("The value of this variable is not 57. It is ", var_2)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Using "elif" to catch specific values, not caught by the "if" statement
int_c = 20

if int_c == 57:
    print("The value of this variable is 57")
elif int_c > 57:
    print("The value of this variable is higher than 57")
else:
    print("The value of this variable is not 57 nor higher than 57. It is ", var_2)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# Please note this is different from using multiple if statements as the if-elif-else sequence is interpreted as an exclusive choice between the different 
# arguments, where the argument that is valid first in sequence will be called.

# In case multiple if statements are used they can all be called if their statement is true, see example below
int_d = 57

if int_d == 57:
    print("The value of this variable is 57")
if (int_d < 60) and (int_d > 50):
    print("The value of this variable is between 50 and 60")
# Only these following statements are signified as a block 
if (int_d < 80) and (int_d > 30):
    print("The value of this variable is between 30 and 80")
else:
    print("The value of this variable is not between 30 and 80. It is ", var_2)

# note this behaves very differently:
if int_d == 57:
    print("The value of this variable is 57")
elif (int_d < 60) and (int_d > 50):
    print("The value of this variable is between 50 and 60")
elif (int_d < 80) and (int_d > 30):
    print("The value of this variable is between 30 and 80")
else:
    print("The value of this variable is not between 30 and 80. It is ", var_2)