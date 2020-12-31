# Python Basics

[Slides](https://docs.google.com/presentation/d/18gRu0YkcW7mqnBnbwF6pWwpPwLOq62JegKYO-cR6Ae0/edit?usp=sharing)

### Useful links:

* [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
* [Rhino Python](https://developer.rhino3d.com/guides/rhinopython/)
* [Grasshopper Python](https://developer.rhino3d.com/guides/rhinopython/your-first-python-script-in-grasshopper/)



## Datatypes

Data Type  | Description | Examples 
---- | ---- | ---- 
Integers | Whole Numbers | -2, -1, 0, 1, 2, 3, 4, 5
Floating-point numbers | Numbers with decimal point |  -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
Strings | Ordered sequence of characters | 'a', 'aa', 'aaa', 'Hello!', '11 cats'
List | Ordered sequence of objects | [10, "Hello", 20.3]
Dictonary | Unordered key : value pairs | {"MyKey" : "Value"}
Tuples | Ordered immutable sequence of objects | (10, "Hello, 20.3)
Set | Unordered collection of unique objects | {"a", "b"}
Bool | Logical value indicating True or False | True / False

## Operators

Operators  | Operation  | Example
---- | ---- | ---- 
`**` | Exponent | 2 ** 3 = 8
`%` | Modulus/Remaider | 22 % 8 = 6
`//` | Integer division | 22 // 8 = 2
`/` | Division | 22 / 8 = 2.75
`*`| Multiplication | 3 * 3 = 9
`-`| Subtraction | 5 - 2 = 3
`+`| Addition | 2 + 2 = 4

Examples of expressions in the interactive shell:
```python
>>> 2 + 3 * 6
20
```
## Variables

## Comparison Operators

Used Example a = 3 and b = 4

Operators  | Operation  | Example
---- | ---- | ---- 
`>` | If the value of left operand is **greater than** the value of right operand, the condition becomes true | (a > b) -> False
`<` | If the value of left operand is **less than** the value of right operand, the condition becomes true. | (a < b) -> True
`==` | If the values of two operands are **equal**, then the condition becomes true.	| (a == b) -> False
`>=` | If the value of left operand is **greater than or equal** to the value of right operand, then condition becomes true. | (a >= b) -> False
`<=` | If the value of left operand is **less than or equal** to the value of right operand, then condition becomes true. | (a <= b) -> True
`!=` | If values of two operands are **not equal**, then condition becomes true. | (a != b) -> True

## If - elif - else statements

Definition
```python
if my_condition is equal a value:
    execute some code
elif my_other_condition is equal another value:
    execute something different
else:
    do something else
```
    
Example
```python
mysite = "afab"
if mysite == "robot lab":
    print("It is part of the DesignFactory")
elif mysite == "afab":
    print("Coding is fun")
else:
    print("I do not know much")
```

`Coding is fun`


## While loop

Definition
* repeats statment(s) while a condition is TRUE
* requires an exit condition
```python
while some_boolean_condition:
    do something
else:
    do something different
```

Example
```python
break_condition = 0
while break_condition < 10:
    break_condition = break_condition + 1
    print(break_condition)
else:
    print("out of while loop")
```

## For loop

* iterating over items of a sequence (usually a list)
```python 
mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print(jelly)
```
* iterating over numbers in range()
> The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration: range(start, stop, step)
```python 
for i in range(0, 10, 2):
    print(i)
```
* iterating over characters in a string
```python 
for letter in "Python":
    print("current letter: ", letter)
```  
* iterating over every key in a dictonary
```python 
d = {"k1":1, "k2":2, "k3":3}
for item in d:
    print(item)
```
* index in range
```python 
print(len(pets))
print(list(range(len(pets))))

for index in range(0,len(pets)):
    print(index, pets[index])
```    
* index and objects in list
```python 
for p,x in enumerate(pets):
    print(p, x)
```
* BREAK: Breaks out of the current closest enclosing loop
* CONTINUE: Goes to the top of the closest enclosing loop
* PASS: Does nothing at all
```python 
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
```

## Lists
* Unlike strings, they are mutable
* elements inside a list can be changed
```python 
>>> spam = ['cat', 'bat', 3, 'elephant']

>>> spam
['cat', 'bat', 'rat', 'elephant']

>>> len(spam)
4
```
* Indexing
```python 
>>> spam = ['cat', 'bat', 3, 'elephant']

positive Index
>>> spam[2]
'2'
negative Index
>>> spam[-1]
'elephant'
```
* Slicing
```python 
>>> spam = ['cat', 'bat', 3, 'elephant']
>>> spam[0:4]
['cat', 'bat', 3, 'elephant']

>>> spam[1:3]
['bat', 3]

>>> spam[:2]
['cat', 'bat']
```
* Reassign
```python
>>> spam = spam + ['add new item']
>>> spam
['cat', 'bat', 3, 'elephant', 'add new item']
```
* Create a new list
```python
>>> spam = ['cat', 'bat', 3, 'elephant']
>>> spam.append('append me!')

>>>spam
['cat', 'bat', 3, 'elephant', 'append me!']
```
## Dictionaries

* **unordered** mappings of stored objects by using a key-value pairing (lists store objects in **ordered** sequence, can therefore be indeced or sliced)
* key value: allows to grab an object without knowing the index location
* {key1:value1, key2:value2} the key itself should always be a string

Definition
```python
>>> my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'} 

>>> my_dict
{'key1': 'value1', 'key2': 'value2', 'key3':'value3'} 

>>>my_dict['key1']
'value1'
```
Example
```python
>>> prices_lookup = {'apples':2.99, 'oranges':1.89}

>>>prices_lookup['apples']
2.99
```
* `d.keys()`: giving all the key inputs
```python
>>> key = {'color': 'pink', 'age': 22}
>>> for k in key.keys():
>>>     print(k)

color
age
```
* `d.values()`: giving all the values
```python
>>> value = {'color': 'pink', 'age': 22}
>>> for v in value.values():
>>>     print(v)

pink
22
```
* `d.items()`: giving the pairings - (result is also a tuple as it is in ())
```python
>>> item = {'color': 'pink', 'age': 22}
>>> for i in item.items():
>>>     print(i)

('color', 'pink')
('age', 22)
```
## Functions
* for creating a clean, *repeatable* code
* allow us to create blocks of code that can be easily executed many times
* without needing to constantly rewrite the entire block of code

Definition
```python
def name_of_funktion(name):
    "
    Docstring explains funktion
    "
    print("Hello" + name)
``` 
Example
```python
>>> def name_function():
>>>     print("Hello")

>>> name_function()
Hello
```
```python
>>> def ran_check(num,low,high):
>>>     if num in range(low,high):
>>>         print (f"{num} is in the range between {low} and {high}")
        
>>> ran_check(5,2,7)
5 is in the range between 2 and 7
```
When creating a function using the **def** statement, you can specify what the **return value** should be with a **return statement**. A return statement consists of the following:
* The return keyword
* The value or expression that the function should return
```python
* Write a function that computes the volume of a sphere given its radius.
* The volume of a sphere is given as $$\frac{4}{3} πr^3$$
>>> import math
>>> def vol(rad=5):
>>>    V = 4/3 * math.pi* rad**3 
>>>    return V

>>> vol()
523.5987755982989
```
```python
* if word starts with a vowel, add "ay" to end
* if word does not start with a vowel, put first letter at the end, then add "ay"

>>> def pig_latin(word):
>>>     first_letter = word[0] 
>>>     if first_letter in "aeiou":
>>>         pig_word = word + "ay"
>>>     else:
>>>         pig_word = word[1:] + first_letter + "ay"        
>>>     return pig_word

>>> pig_latin("apple")
'appleay'
```

## Classes
Dataclasses are python classes but are suited for storing data objects. This module provides a decorator and functions for automatically adding generated special methods such as **__init__()** and **__repr__()** to user-defined classes.
* Storing data and representing certain data type 
* Comparing to other objects of the same type

`self.` 
* representing the instance of a class 
* accessing the attributes and methods of the class in python

`__init__()` 
* A reseved method in python classes 
* Called as constructor in object oriented terminology: Called when an object is created from a class and allows the class to initialize the attributes of the class
```python
>>> class Vehicle():
>>>     def __init__(self, colour, nb_wheels, name):
>>>         self.colour = colour
>>>         self.nb_wheels = nb_wheels
>>>         self.name = name
>>> vehicle_1 = Vehicle("blue", 2, "bike")
>>> vehicle_2 = Vehicle("red", 4, "car")

>>> print("This is a " + vehicle_1.colour + " " + vehicle_1.name + " with ", vehicle_1.nb_wheels, " " + "wheels")
This is a blue bike with  2  wheels
>>> print("This is a " + vehicle_2.colour + " " + vehicle_2.name + " with " + str(vehicle_2.nb_wheels) + " " + "wheels")
This is a red car with 4 wheels
```
```python
>>> Find out the cost of a rectangular field with breadth(b=120), length(l=160). It costs x (2000) rupees per 1 square unit
>>> class Rectangle:
>>>    def __init__(self, length, breadth, unit_cost=0):
>>>        self.length = length
>>>        self.breadth = breadth
>>>        self.unit_cost = unit_cost
>>>    def get_area(self):
>>>        return self.length * self.breadth
>>>    def calculate_cost(self):
>>>        area = self.get_area()
>>>        return area * self.unit_cost
>>> r = Rectangle(160, 120, 2000)
>>> print("Area of Rectangle: %s sq units" % (r.get_area()))

Area of Rectangle: 19200 sq units
```
## Import
* getting access to code from another module by importing file/function

* import **module_name**:
```python
>>> import math
>>> print(math.pi)

3.141592653589793
```
* import **module_name.member_name**
```python
>>> from math import pi 
>>> print(pi) 

3.141592653589793
```

* to get **COMPAS** working in Grasshopper

In Grasshopper, COMPAS is imported from within a GhPython component. To verify that everything is working properly, simply create a GhPython component on your Grasshopper canvas, paste the following script and hit OK

```python
>>> import compas

>>> from compas.datastructures import Mesh
>>> from compas_ghpython.artists import MeshArtist
>>> mesh = Mesh.from_obj(compas.get('faces.obj'))

>>> artist = MeshArtist(mesh)

>>> a = artist.draw_mesh()
```
