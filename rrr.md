# Loops in Python

Welcome! This notebook will teach you about the loops in the Python Programming Language.  
By the end of this lab, you'll know how to use the loop statements in Python, including `for` loop and `while` loop.

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

Sometimes, you might want to repeat a given operation many times. Repeated executions like this are performed by **loops**.  
We will look at two types of loops: `for` loops and `while` loops.

Before we discuss loops, let's discuss the `range` object. It is helpful to think of the `range` object as an ordered list.  
For now, let's look at the simplest case. If we would like to generate an object that contains elements ordered from 0 to 2, we simply use the following command:

---

## What is for loop?

### For loop example

```python
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])
 
The code in the indent is executed N times. Each time, the value of i is increased by 1 for every execution.
The statement executed is to print out the value in the list at index i.

Print sequence from 0 to 7:
python
Copy
Edit
for i in range(0, 8):
    print(i)
Loop directly through a list
python
Copy
Edit
dates = [1982, 1980, 1973]

for year in dates:  
    print(year)
For each iteration, the value of the variable year behaves like the value of dates[i] in the first example.

Use for loop to change the elements in a list
python
Copy
Edit
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square", i, 'is', squares[i])
    squares[i] = 'white'
    print("After square", i, 'is', squares[i])
Loop through the list and iterate on both index and element value
python
Copy
Edit
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
What is while loop?
As you can see, the for loop is used for a controlled flow of repetition.
However, what if we don't know when we want to stop the loop?
What if we want to keep executing a code block until a certain condition is met?

The while loop exists as a tool for repeated execution based on a condition.
The code block will keep being executed until the given logical condition returns False.

Let’s say we would like to iterate through list dates and stop at the year 1973, then print out the number of iterations.
This can be done with the following block of code:

While Loop Example
python
Copy
Edit
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]

print("It took", i, "repetitions to get out of loop.")
A while loop iterates until the condition in the argument is not met, as shown in the example above.