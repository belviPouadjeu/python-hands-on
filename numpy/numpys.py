"""
NumPy Array Basics Example

This script demonstrates basic NumPy array creation and element access.
"""

import numpy as np

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#Checking NumPy Version
print(np.__version__)

# Check the type of the array
type = type(a)
print(type)

#Check the type of the array and Value type for the given array b

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
#type = type(b)
typeOne = b.dtype
print(typeOne)

#Assign valueWe can change the value of the array. Consider the array c:
c = np.array([20, 1, 2, 3, 4])
c[0] = 100
print(c)


# Slicing the numpy array
d = c[1:4]
print(d)
c[3:5] = 300, 400
print('Valuer of d:',d)
print('Value of c:',c)

 # We can also define the steps in slicing, like this: [start:end:step].
 arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])


 # If we don't pass start its considered 0
 print(arr[:4])

 # If we don't pass end its considered length of array
 print(arr[4:])

 # If we don't pass step its considered 1
 print(arr[::])

# Try it yourself
# Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[arr % 2 == 0])
print(arr[::2])
print(arr[1:8:2])
