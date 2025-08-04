Sets in Python
Estimated time needed: 20 minutes

Objectives
After completing this lab you will be able to:

Work with sets in Python, including operations and logic operations.

Table of Contents
Sets
Set Content
Set Operations
Sets Logic Operations
Quiz on Sets

Sets
Set Content
A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}. Python will automatically remove duplicate items:

# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1

 Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set

Now let us create a set of genres:

 Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres


Set Operations
Let us go over set operations, as these can be used to change the set. Consider the set A:

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A

We can add an element to a set using the add() method:
# Add element to set

A.add("NSYNC")
A

# Add element to set

A.add("NSYNC")
A

# Try to add duplicate element to the set

A.add("NSYNC")
A

We can remove an item from a set using the remove method:

# Remove the element from set

A.remove("NSYNC")
A

We can verify if an element is in the set using the in command:

# Verify if the element is in the set

"AC/DC" in A


Sets Logic Operations
Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:

Consider the following two sets:

Sets Logic Operations
Remember that with sets you can check the difference between sets, as well as the symmetric difference, intersection, and union:

Consider the following two sets:

# Print two sets

album_set1, album_set2

You can find the intersect of two sets as follow using &:

# Find the intersections

intersection = album_set1 & album_set2
intersection


You can find all the elements that are only contained in album_set1 using the difference method:

# Find the difference in set1 but not set2

album_set1.difference(album_set2)  

album_set2.difference(album_set1)  

You can also find the intersection of album_list1 and album_list2, using the intersection method:

# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   

The union corresponds to all the elements in both sets, which is represented by coloring both circles:
The union is given by:

# Find the union of two sets

album_set1.union(album_set2)

nd you can check if a set is a superset or subset of another set, respectively, like this:

# Check if superset

set(album_set1).issuperset(album_set2)   

# Check if subset

set(album_set2).issubset(album_set1)     
# Check if subset

set(album_set2).issubset(album_set1)     

# Check if subset

set(album_set2).issubset(album_set1)     

# Check if subset

set(album_set2).issubset(album_set1)     

# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 
# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})   