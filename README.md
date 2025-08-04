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


