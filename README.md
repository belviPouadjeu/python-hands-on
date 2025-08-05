# Sets in Python

**Estimated time needed**: 20 minutes

---

## Objectives

After completing this lab, you will be able to:

- Work with sets in Python, including operations and logic operations.

---

## Table of Contents

- [Sets](#sets)
- [Set Content](#set-content)
- [Set Operations](#set-operations)
- [Sets Logic Operations](#sets-logic-operations)
- [Intersections](#intersections)
- [Differences](#differences)
- [Union](#union)
- [Subset and Superset](#subset-and-superset)
- [Quiz on Sets](#quiz-on-sets)

---

## Sets

### Set Content

A **set** is a unique collection of objects in Python. You can denote a set with a pair of curly brackets `{}`. Python will automatically remove duplicate items:

```python
# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)
```

## Convert a list to a set:

```python
album_list = [
    "Michael Jackson", "Thriller", 1982, "00:42:19",
    "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0
]

album_set = set(album_list)
print(album_set)

```
## Add Elements

```python
# Add element to set
A.add("NSYNC")
print(A)

# Try to add duplicate element
A.add("NSYNC")
print(A)

```

## Remove Elements

```python
# Remove the element from set
A.remove("NSYNC")
print(A)
```

## Membership Test
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

## Intersssection

```python
# Find the intersections
intersection = album_set1 & album_set2
print(intersection)

# Or use the method
print(album_set1.intersection(album_set2))
```

## Differences
```python
# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))

# Find the difference in set2 but not set1
print(album_set2.difference(album_set1))
```

## Union

```python
# Find the union of two sets
album_set3 = album_set1.union(album_set2)
print(album_set3)

```

## Subset and Superset
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

# 🧠 Quiz on Sets

Try these on your own:

1. **What happens when you convert a list with duplicates to a set?**
   - Hint: Think about how sets handle uniqueness.

2. **What is the result of `set1 & set2` vs `set1 | set2`?**
   - Tip: One is intersection, the other is union. What do they return?

3. **How does Python treat membership in sets (`in` keyword)?**
   - Consider performance and how it differs from lists.

4. **When is a set a subset or superset of another?**
   - Use `.issubset()` and `.issuperset()` methods or comparison operators like `<=` and `>=`.


Loops in Python
Welcome! This notebook will teach you about the loops in the Python Programming Language. By the end of this lab, you'll know how to use the loop statements in Python, including for loop, and while loop.

Table of Contents

Table of Contents
Loops
Range
What is for loop?
What is while loop?
Quiz on Loops

Loops
Range
Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by loops. We will look at two types of loops, for loops and while loops.

Before we discuss loops lets discuss the range object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate an object that contains elements ordered from 0 to 2 we simply use the following command:

Loops
Range
Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by loops. We will look at two types of loops, for loops and while loops.

Before we discuss loops lets discuss the range object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate an object that contains elements ordered from 0 to 2 we simply use the following command:

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) 

The code in the indent is executed N times, each time the value of i is increased by 1 for every execution. The statement executed is to print out the value in the list at index i as shown here: 

In this example we can print out a sequence of numbers from 0 to 7:

# Example of for loop

for i in range(0, 8):
    print(i)

In Python we can directly access the elements in the list as follows:

# Exmaple of for loop, loop through list

for year in dates:  
    print(year) 

For each iteration, the value of the variable year behaves like the value of dates[i] in the first example:
We can change the elements in a list:

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

We can access the index and the elements of a list as follows:

We can access the index and the elements of a list as follows:

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

What is while loop?
As you can see, the for loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.

Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")

A while loop iterates merely until the condition in the argument is not met, as shown in the following figure: