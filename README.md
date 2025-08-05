# Python Programming Guide

**Estimated time needed**: 60 minutes

---

## Table of Contents

- [Sets in Python](#sets-in-python)
- [Loops in Python](#loops-in-python)
- [Functions in Python](#functions-in-python)

---

# Sets in Python

## Objectives

After completing this section, you will be able to:

- Work with sets in Python, including operations and logic operations
- Understand set uniqueness and basic operations
- Perform set logic operations like intersection, union, and difference

## Set Content

A **set** is a unique collection of objects in Python. You can denote a set with a pair of curly brackets `{}`. Python will automatically remove duplicate items:

```python
# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)
```

### Convert a list to a set

```python
album_list = [
    "Michael Jackson", "Thriller", 1982, "00:42:19",
    "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0
]

album_set = set(album_list)
print(album_set)
```

### Add Elements

```python
# Add element to set
A.add("NSYNC")
print(A)

# Try to add duplicate element
A.add("NSYNC")
print(A)
```

### Remove Elements

```python
# Remove the element from set
A.remove("NSYNC")
print(A)
```

### Membership Test

```python
# Verify if the element is in the set
print("AC/DC" in A)
```

## Sets Logic Operations

You can check for difference, symmetric difference, intersection, and union between sets.

```python
# Define two sets
album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
```

### Intersection

```python
# Find the intersections
intersection = album_set1 & album_set2
print(intersection)

# Or use the method
print(album_set1.intersection(album_set2))
```

### Differences

```python
# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))

# Find the difference in set2 but not set1
print(album_set2.difference(album_set1))
```

### Union

```python
# Find the union of two sets
album_set3 = album_set1.union(album_set2)
print(album_set3)
```

### Subset and Superset

You can check if a set is a superset or subset of another:

```python
# Check if album_set1 is a superset of album_set2
print(album_set1.issuperset(album_set2))

# Check if album_set2 is a subset of album_set1
print(album_set2.issubset(album_set1))

# More examples
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))
print(album_set1.issuperset({"Back in Black", "AC/DC"}))
```

## 🧠 Quiz on Sets

Try these on your own:

1. **What happens when you convert a list with duplicates to a set?**
   - Hint: Think about how sets handle uniqueness.

2. **What is the result of `set1 & set2` vs `set1 | set2`?**
   - Tip: One is intersection, the other is union. What do they return?

3. **How does Python treat membership in sets (`in` keyword)?**
   - Consider performance and how it differs from lists.

4. **When is a set a subset or superset of another?**
   - Use `.issubset()` and `.issuperset()` methods or comparison operators like `<=` and `>=`.

---

# Loops in Python

## Objectives

By the end of this section, you'll know how to use the loop statements in Python, including `for` loop and `while` loop.

## Range

Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by **loops**. We will look at two types of loops: `for` loops and `while` loops.

Before we discuss loops, let's discuss the `range` object. It is helpful to think of the `range` object as an ordered list.

## For Loops

### Basic For Loop Example

```python
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])
```

The code in the indent is executed N times. Each time, the value of i is increased by 1 for every execution.

### Print sequence from 0 to 7

```python
for i in range(0, 8):
    print(i)
```

### Loop directly through a list

```python
dates = [1982, 1980, 1973]

for year in dates:  
    print(year)
```

For each iteration, the value of the variable year behaves like the value of dates[i] in the first example.

### Use for loop to change the elements in a list

```python
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square", i, 'is', squares[i])
```

### Loop through the list and iterate on both index and element value

```python
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
```

## While Loops

As you can see, the for loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met?

The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns False.

### While Loop Example

```python
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]

print("It took", i, "repetitions to get out of loop.")
```

A while loop iterates until the condition in the argument is not met, as shown in the example above.

---

# Functions in Python

## Objectives

After completing this section, you will be able to:

- Understand what functions are and how to create them
- Work with function parameters and return values
- Understand variable scope (local vs global)
- Use built-in functions effectively

## What is a Function?

A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.

There are two types of functions:

- **Pre-defined functions** (built-in)
- **User defined functions**

### Function Definition Rules

Here are simple rules to define a function in Python:

- Functions blocks begin with `def` followed by the function name and parentheses `()`
- Input parameters or arguments should be placed within these parentheses
- There is a body within every function that starts with a colon `:` and is indented
- You can place documentation before the body
- The `return` statement exits a function, optionally passing back a value

### Basic Function Example

```python
# First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

# Call the function add()
add(1)
add(2)
```

### Function with Multiple Parameters

```python
# Define a function for multiplying two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')  # This line never executes
    
result = Mult(12, 2)
print(result)
```

### Functions with Different Data Types

```python
# Use mult() multiply two integers
Mult(2, 3)

# Use mult() multiply two floats
Mult(10.0, 3.14)

# Use mult() multiply string and integer
Mult(2, "The BodyGuard ")
```

## Variables and Scope

The input to a function is called a **formal parameter**.

- A variable that is declared inside a function is called a **local variable**
- A variable that is declared outside a function definition is a **global variable**

```python
# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Global variable
x = 3
# Makes function call and return function a y
y = square(x)
```

## Pre-defined Functions

There are many pre-defined functions in Python:

```python
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together
sum(album_ratings)

# Show the length of the list or tuple
len(album_ratings)
```

## Using if/else Statements and Loops in Functions

```python
# Function example
def type_of_album(album, year_released):
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1980)
print(x)
```

### Print the list using for loop

```python
def PrintList(the_list):
    for element in the_list:
        print(element)

# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])
```

## Setting Default Argument Values

```python
# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good its rating is", rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)
```

## Global vs Local Variables

```python
# Example of global variable
album = "The BodyGuard"

def printer1(album):
    internal_var1 = "Thriller"
    print(album, "is an album")
    
printer1(album)

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"  # Local variable
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)  # Global variable
```

## Collections and Functions

When the number of arguments are unknown for a function, they can all be packed into a tuple:

```python
def printAll(*args):  # All the arguments are 'packed' into args
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)

# printAll with 3 arguments
printAll('Horsefeather', 'Adonis', 'Bone')

# printAll with 4 arguments
printAll('Sidecar', 'Long Island', 'Mudslide', 'Carriage')
```

Similarly, the arguments can also be packed into a dictionary:

```python
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada', Province='Ontario', City='Toronto')
```

## Quiz on Functions

1. **Come up with a function that divides the first input by the second input:**

```python
def divide(a, b):
    return a / b
```

2. **Write a function to find total count of word "little" in the given string:**

```python
def count_little(text):
    words = text.lower().split()
    return words.count('little')

# Test string
test_string = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"

print(count_little(test_string))
```

---

## Summary

This guide covered three fundamental Python concepts:

1. **Sets**: Unique collections with operations like union, intersection, and difference
2. **Loops**: For loops and while loops for repetitive operations
3. **Functions**: Reusable code blocks with parameters, return values, and scope considerations

Practice these concepts to build a strong foundation in Python programming!

# Classes and Objects in Python

## Table of Contents
Introduction to Classes and Objects
Creating a class
Instances of a Class: Objects and Attributes
Methods
Creating a class
Creating an instance of a class Circle
The Rectangle Class

### Introduction to Classes and Objects
- Creating a Class
The first step in creating a class is giving it a name. In this notebook, we will create two classes: Circle and Rectangle. We need to determine all the data that make up that class, which we call attributes. Think about this step as creating a blue print that we will use to create objects. In figure 1 we see two classes, Circle and Rectangle. Each has their attributes, which are variables. The class Circle has the attribute radius and color, while the Rectangle class has the attribute height and width. Let’s use the visual examples of these shapes before we get to the code, as this will help you get accustomed to the vocabulary.

####  Instances of a Class: Objects and Attributes
An instance of an object is the realisation of a class, and in Figure 2 we see three instances of the class circle. We give each object a name: red circle, yellow circle, and green circle. Each object has different attributes, so let's focus on the color attribute for each object.

The colour attribute for the red Circle is the colour red, for the green Circle object the colour attribute is green, and for the yellow Circle the colour attribute is yellow.

#### Methods
Methods give you a way to change or interact with the object; they are functions that interact with objects. For example, let’s say we would like to increase the radius of a circle by a specified amount. We can create a method called add_radius(r) that increases the radius by r. This is shown in figure 3, where after applying the method to the "orange circle object", the radius of the object increases accordingly. The “dot” notation means to apply the method to the object, which is essentially applying a function to the information in the object.

## Creating a Class
Now we are going to create a class Circle, but first, we are going to import a library to draw the objects:

```python
# Import the library

import matplotlib.pyplot as plt
%matplotlib inline  
```

The next step is a special method called a constructor __init__, which is used to initialize the object. The inputs are data attributes. The term `self` contains all the attributes in the set. For example the `self.color` gives the value of the attribute color and `self.radius` will give you the radius of the object. We also have the method `add_radius()` with the parameter `r`, the method adds the value of r to the attribute radius. To access the radius we use the syntax `self.radius`. The labeled syntax is 

The actual object is shown below. We include the method     `drawCircle` to display the image of a circle. We set the default radius to 3 and the default colour to blue:

```python
# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
```

### Creating an instance of a class Circle
Let’s create the object RedCircle of type Circle to do the following:

```python
# Create an object RedCircle

RedCircle = Circle(10, 'red')
```

We can use the `dir` command to get a list of the object's methods. Many of them are default Python methods.

```python
# Find out the methods can be used on the object RedCircle

dir(RedCircle)
```

We can look at the data attributes of the object:

### Print the object attribute radius
`RedCircle.radius`

#### Print the object attribute color
`RedCircle.color`

### Call the method drawCircle
`RedCircle.drawCircle()`

We can increase the radius of the circle by applying the method `add_radius()`. Let's increases the radius by 2 and then by 5:


```python
# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)
```
Let’s create a blue circle. As the default colour is blue, all we have to do is specify what the radius is:

#### Create a blue circle with a given radius

`BlueCircle = Circle(radius=100)`

As before, we can access the attributes of the instance of the class by using the dot notation:


#### Print the object attribute radius
`BlueCircle.radius`

 #### Print the object attribute color

`BlueCircle.color`

We can draw the object by using the method `drawCircle()`:

Compare the x and y axis of the figure to the figure for `RedCircle`; they are different.

## The Rectangle Class
Let's create a class rectangle with the attributes of height, width, and color. We will only add the method to draw the rectangle object:

```python
# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
```

Let’s create the object `SkinnyBlueRectangle` of type Rectangle. Its width will be 2 and height will be 3, and the color will be blue:

#### Create a new object rectangle

`SkinnyBlueRectangle = Rectangle(2, 3, 'blue')`

As before we can access the attributes of the instance of the class by using the dot notation:

#### Print the object attribute height

`SkinnyBlueRectangle.height`

#### Print the object attribute width

`SkinnyBlueRectangle.width`

#### Print the object attribute color

`SkinnyBlueRectangle.color`

We can draw the object:

#### Use the drawRectangle method to draw the shape

`SkinnyBlueRectangle.drawRectangle()`

Let’s create the object FatYellowRectangle of type Rectangle:

#### Create a new object rectangle

`FatYellowRectangle = Rectangle(20, 5, 'yellow')`

We can access the attributes of the instance of the class by using the dot notation:

#### Print the object attribute height
`FatYellowRectangle.height`

#### Print the object attribute width

`FatYellowRectangle.width`

#### Print the object attribute color

`FatYellowRectangle.color`

We can draw the object:

#### Use the drawRectangle method to draw the shape

`FatYellowRectangle.drawRectangle()`

### Scenario: Car dealership's inventory management system
You are working on a Python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately.

- Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.

- Task-2. Update the class with the default color for all vehicles," white"

- Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.

- Task-4. Create a method to display all the properties of an object of the class.

- Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.



