# Loops in Python

Welcome! This notebook will teach you about the loops in the Python Programming Language. By the end of this lab, you'll know how to use the loop statements in Python, including for loop, and while loop.

**Estimated time needed**: 30 minutes

---

## Table of Contents

- [Loops](#loops)
- [Range](#range)
- [What is for loop?](#what-is-for-loop)
- [What is while loop?](#what-is-while-loop)
- [Quiz on Loops](#quiz-on-loops)

---

## Loops

### Range

Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by loops. We will look at two types of loops, for loops and while loops.

Before we discuss loops let's discuss the range object. It is helpful to think of the range object as an ordered list. For now, let's look at the simplest case. If we would like to generate an object that contains elements ordered from 0 to 2 we simply use the following command:

```python
# Create a range object
range(3)
```

---

## What is for loop?

### Basic For Loop Example

```python
# For loop example
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])
```

The code in the indent is executed N times, each time the value of i is increased by 1 for every execution. The statement executed is to print out the value in the list at index i as shown here.

### Range with Start and Stop

In this example we can print out a sequence of numbers from 0 to 7:

```python
# Example of for loop
for i in range(0, 8):
    print(i)
```

### Direct List Iteration

In Python we can directly access the elements in the list as follows:

```python
# Example of for loop, loop through list
for year in dates:  
    print(year)
```

For each iteration, the value of the variable year behaves like the value of dates[i] in the first example.

### Modifying List Elements

We can change the elements in a list:

```python
# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is', squares[i])
```

### Using enumerate()

We can access the index and the elements of a list as follows:

```python
# Loop through the list and iterate on both index and element value
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
```

---

## What is while loop?

As you can see, the for loop is used for a controlled flow of repetition. However, what if we don't know when we want to stop the loop? What if we want to keep executing a code block until a certain condition is met? The while loop exists as a tool for repeated execution based on a condition. The code block will keep being executed until the given logical condition returns a False boolean value.

Let's say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations. This can be done with the following block of code:

```python
# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i, "repetitions to get out of loop.")
```

A while loop iterates merely until the condition in the argument is not met, as shown in the following figure.

---

## 🧠 Quiz on Loops

Try these on your own:

1. **What is the difference between a for loop and a while loop?**
   - Hint: Think about when you know the number of iterations vs. when you don't.

2. **What does the range() function return?**
   - Try: `print(type(range(5)))` and `print(list(range(5)))`

3. **How can you loop through a list and get both the index and value?**
   - Tip: There's a built-in function that makes this easy.

4. **What happens if you modify a list while iterating through it?**
   - Consider the potential issues and best practices.

5. **How would you create a while loop that runs indefinitely?**
   - Warning: Be careful with infinite loops!
