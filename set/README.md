# 🎵 Python Sets Overview

## Set Content
A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}. Python will automatically remove duplicate items:

## 🔹 What Are Sets?

Sets are a type of **collection** in Python. Like lists and tuples:
- They can store different Python types.
- They are defined using **curly brackets `{}`**.

Unlike lists and tuples:
- Sets are **unordered** (they do not record element positions).
- Sets contain **only unique elements** (no duplicates allowed).

### 🧪 Example: Defining a Set

```python
my_set = {"AC/DC", "Back in Black", "AC/DC"}
print(my_set)  # Output: {'AC/DC', 'Back in Black'}
```
Notice how the duplicate `"AC/DC"` is removed automatically.

## 🔄 Converting Lists to Sets  
You can convert a list to a set using the `set()` function — this is called **type casting**.  

### 🧪 Example:  

```python
# Original list with duplicates
artists_list = ["AC/DC", "Back in Black", "Thriller", "AC/DC"]

# Convert to set (removes duplicates)
artists_set = set(artists_list)

print(artists_set)  # Output: {'AC/DC', 'Back in Black', 'Thriller'}
```

## ⚙️ Set Operations

### ➕ Adding Elements
Use the `.add()` method:

```python
my_set = {"apple", "banana"}
my_set.add("orange")
print(my_set)  # Output: {'apple', 'banana', 'orange'}
```

### Key points:

- Adds a single element to the set

- If the element already exists, the set remains unchanged (no duplicates)

- Modifies the set in place (does not return a new set)

- Example with duplicate:

## ➖ Removing Elements
Use the `.remove()` method:

```python
A = {"AC/DC", "Back in Black", "NSYNC"}
A.remove("NSYNC")
print(A)  # Output: {'AC/DC', 'Back in Black'}
```
Note: Raises KeyError if the element doesn't exist. Use .discard() to avoid this.

### 🔍 Checking Membership
Use the in keyword:

```python
A = {"AC/DC", "Back in Black"}
print("AC/DC" in A)  # True
print("Who" in A)    # False
```

### 🔣 Mathematical Set Operations
- 🎯 Intersection
Elements common to both sets:

```python
album_set_1 = {"AC/DC", "Back in Black", "NSYNC"}
album_set_2 = {"AC/DC", "Back in Black", "Who"}

album_set_3 = album_set_1 & album_set_2
print(album_set_3)  # Output: {'AC/DC', 'Back in Black'}
```
- Alternative method

```python
album_set_1.intersection(album_set_2)
```

### 🔗 Union
All elements from both sets:

```python
album_union = album_set_1 | album_set_2
print(album_union)  # Output: {'AC/DC', 'Back in Black', 'NSYNC', 'Who'}
```
Alternative method:

```python
album_set_1.union(album_set_2)
```
🧩 Subset Check
Check if one set is contained in another:

```python
album_set_3 = {"AC/DC", "Back in Black"}
print(album_set_3.issubset(album_set_1))  # True
```
# Equivalent check:
```python
album_set_3 <= album_set_1
print(album_set_3 <= album_set_1)  # True
For proper subset (strictly contained with fewer elements):
```

```python
print(album_set_3 < album_set_1)  # True
```