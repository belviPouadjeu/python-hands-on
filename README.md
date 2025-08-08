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


# Write and Save Files in Python

Objectives
After completing this lab you will be able to:

Write to files using Python libraries

## Table of Contents
Writing Files
Appending Files
Additional File modes
Copy a File

### Writing Files
We can open a file object using the method write() to save the text file to a list. To write to a file, the mode argument must be set to w. Let’s write a file Example2.txt with the line: “This is line A”

```python
# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
```

We can read the file to see if it worked:

```python
# Read file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
```

The method `.write()` works similar to the method .readline(), except instead of reading a new line it writes a new line. The process is illustrated in the figure. The different colour coding of the grid represents a new line added to the file after each method call.

You can check the file to see if your results are correct
```python
# Check whether write to file

with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
```

We write a list to a .txt file as follows:
```python
# Sample list of text

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
```
```python
# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
```
We can verify the file is written by reading it and printing out the values:
```python
# Verify if writing to file is successfully executed

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```

However, note that setting the mode to w overwrites all the existing data in the file.

```python
with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
```

## Appending Files
We can write to files without losing any of the existing data as follows by setting the mode argument to append: a. you can append a new line as follows:
```python
# Write a new line to text file

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
```
```python
# Verify if the new line is in the text file

with open('Example2.txt', 'r') as testwritefile:
```

## Additional modes
It's fairly ineffecient to open the file in a or w and then reopening it in r to read any lines. Luckily we can access the file in the following modes:

r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.
Let's try out the a+ mode:
```python
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
```
There were no errors but read() also did not output anything. Why not? Let's take a look at write() and read() under the a+ mode:
```python
# Opening the file in a+ mode and writing multiple lines
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
    testwritefile.seek(0)
    print(testwritefile.read())
```

Most of the file methods we've looked at work in a certain location in the file. .write()  writes at a certain location in the file. `.read()` reads at a certain location in the file and so on. You can think of this as moving your pointer around in the notepad to make changes at specific location.

Opening the file in w is akin to opening the .txt file, moving your cursor to the beginning of the text file, writing new text and deleting everything that follows. Whereas opening the file in a is similiar to opening the .txt file, moving your cursor to the very end and then adding the new pieces of text.
It is often very useful to know where the 'cursor' is in a file and be able to control it. The following methods allow us to do precisely this -

`.tell()` - returns the current position in bytes
`.seek(offset,from)` - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end
Now lets revisit a+

```python
with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )
```

Finally, a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however, opening a file in w+ overwrites it and deletes all pre-existing data.

In the following code block, Run the code as it is first and then run it without the `.truncate()`.

```python
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())
```

To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a `.truncate()` method at the end of your data. This will reduce the file to your data and delete everything that follows.

```python
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    
```

## Copy a File
Let's copy the file Example2.txt to the file Example3.txt:
```python
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
```
We can read the file to see if everything works:
```python
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
```

After reading files, we can also write data into files and save them in different file formats like .txt, .csv, .xls (for excel files) etc. You will come across these in further examples

NOTE: If you wish to open and view the example3.txt file, download this lab here and run it locally on your machine. Then go to the working directory to ensure the example3.txt file exists and contains the summary data that we wrote.

### Exercise (File)
Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.



# Hands-on Lab: Loading data with Pandas

## Objectives : Use Pandas to access and view data

### Table of Contents
- About the Dataset
- Introduction of Pandas
- Viewing Data and Accessing Data
- Quiz on DataFrame

### About the Dataset
The table has one row for each product and several columns.

 - OrderID: A unique identifier for each order
 - Product: The name of the product purchased
 - Category: The category to which the product belongs (e.g., Electronics, Furniture,        Stationery)
 - Quantity: The number of units purchased for that product
 - Price: The price per unit of the product
 - Total: The total cost for the product (calculated as Quantity × Price)
 - OrderDate: The date when the order was placed
 - CustomerCity: The city where the customer resides

 ### Introduction of Pandas

 ```python
 # Dependency needed to install file 

%pip install xlrd openpyxl
 ```

 ```python
 # Import required library

import pandas as pd
 ```

After the import command, we now have access to a large number of pre-built classes and functions. This assumes the library is installed; in our lab environment all the necessary libraries are installed. One way pandas allows you to work with data is a dataframe. Let's go through the process to go from a comma separated values (.csv) file to a dataframe. This variable `csv_path` stores the path of the .csv, that is used as an argument to the `read_csv` function. The result is stored in the object `df`, this is a common short form used for a variable referring to a Pandas dataframe.

```python
 Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Product-sales.csv")
df = pd.read_csv("Product-sales.csv")
```

Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface. While working on the downloaded version of this notebook on their local machines, the learners can simply skip the steps above, and simply use the URL directly in the `pandas.read_csv()` function. You can uncomment and run the statements in the cell below.

```python
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
#df = pd.read_csv(filename)
```

We can use the method `head()` to examine the first five rows of a dataframe:
```python
# show the first five rows using dataframe.head() method
df.head()
```

We use the path of the excel file and the function `read_excel`. The result is a data frame as before:
```python
# Read data from Excel File and print the first five rows
# Read data from Excel File and print the first five rows

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'

await download(xlsx_path, "Product-sales.xlsx")
df = pd.read_excel("Product-sales.xlsx")
df.head()
```
Note: This version of the lab is working on JupyterLite, which requires the dataset to be downloaded to the interface. While working on the downloaded version of this notebook on their local machines, the learners can simply skip the steps above, and simply use the URL directly in the `pandas.read_excel()` function. You can uncomment and run the statements in the cell below.

```python
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
#df = pd.read_excel(xlsx_path)
```

We can access the column Quantity and assign it a new dataframe `x`:

```python
# Access to the column Quantity
x = df[['Quantity']]
x
```

## Viewing Data and Accessing Data
You can also get a column as a series. You can think of a Pandas series as a 1-D dataframe. Just use one bracket:

```python
# Get the column as a series
x = df['Product']
x
```

You can also get a column as a dataframe. For example, we can assign the column Quantity:
```python
# Get the column as a dataframe

x = df[['Quantity']]
type(x)
```

You can do the same thing for multiple columns; we just put the dataframe name, in this case, `df`, and the name of the multiple column headers enclosed in double brackets. The result is a new dataframe comprised of the specified columns:
```python
# Access to multiple columns

y = df[['Product','Category', 'Quantity']]
y
```

```python
# Access the value on the first row and the first column

df.iloc[0, 0]
```

You can access the 2nd row and the 1st column as follows:

```python
# Access the 2nd row and the 1st column

df.iloc[1,0]
```

You can access the 1st row and the 3rd column as follows:
```python
# Access the 1st row and the 3rd column

df.iloc[0,2]
```
```pyhon
## Access the value on the second row and the third column
df.iloc[1,2]
```

You can access the column using the name as well, the following are the same as above:

```python
# Access the column using the name

df.loc[0, 'Product']

# Access the column using the name

df.loc[1, 'Product']

# Access the column using the name

df.loc[1, 'CustomerCity']

# Access the column using the name

df.loc[1, 'Total']
```

You can perform slicing using both the index and the name of the column:
```python
# Slicing the dataframe

df.iloc[0:2, 0:3]

# Slicing the dataframe using name

df.loc[0:2, 'OrderID':'Category']
```
### Quiz on DataFrame
 - 
 Use a variable `q` to store the column Price as a dataframe
 - 
 Assign the variable q to the dataframe that is made up of the column Product and Category
 - 
 Access the 2nd row and the 3rd column of ``df``


 # 1D Numpy in Python¶

## What is Numpy?
**NumPy** is a Python library used for working with arrays, linear algebra, fourier transform, and matrices. NumPy stands for Numerical Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

NumPy is usually imported under the np alias.

It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing `numpy`:


