# Sets in Python

**Estimated time needed**: 20 minutes

## Objectives

After completing this lab you will be able to:

- Work with sets in Python, including operations and logic operations.

---

## Table of Contents

- [Sets](#sets)
- [Set Content](#set-content)
- [Set Operations](#set-operations)
- [Sets Logic Operations](#sets-logic-operations)
- [Quiz on Sets](#quiz-on-sets)

---

## Sets

### Set Content

A **set** is a unique collection of objects in Python. You can denote a set with a pair of curly brackets `{}`. Python will automatically remove duplicate items:

```python
# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1
```

## Convert list to set

```python
album_list = [
    "Michael Jackson", "Thriller", 1982, "00:42:19",
    "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0
]
album_set = set(album_list)
album_set
```
Now let us create a set of genres:
Now let us create a set of genres:

python

# Convert list to set
music_genres = set([
    "pop", "pop", "rock", "folk rock", "hard rock", "soul",
    "progressive rock", "soft rock", "R&B", "disco"
])
music_genres
Set Operations
Let us go over set operations, as these can be used to change the set. Consider the set A:

python

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
A
We can add an element to a set using the add() method:

python

# Add element to set
A.add("NSYNC")
A

# Try to add duplicate element
A.add("NSYNC")
A
We can remove an item from a set using the remove() method:

python

# Remove the element from set
A.remove("NSYNC")
A
We can verify if an element is in the set using the in keyword:

python

# Verify if the element is in the set
"AC/DC" in A
Sets Logic Operations
You can check the difference, symmetric difference, intersection, and union between sets.

Consider the following two sets:

python

# Print two sets
album_set1, album_set2
Intersections
python

# Find the intersections
intersection = album_set1 & album_set2
intersection
Differences
python

# Find the difference in set1 but not set2
album_set1.difference(album_set2)

# Find the difference in set2 but not set1
album_set2.difference(album_set1)
- Intersection Method

```python
# Use intersection method to find the intersection
album_set1.intersection(album_set2)
```
- Union
The union corresponds to all elements in both sets:

python

# Find the union of two sets
album_set1.union(album_set2)
Subset and Superset
You can check if a set is a superset or subset of another:

python

# Check if superset
set(album_set1).issuperset(album_set2)

# Check if subset
set(album_set2).issubset(album_set1)

# More examples
set({"Back in Black", "AC/DC"}).issubset(album_set1)

album_set1.issuperset({"Back in Black", "AC/DC"})
