# ============================================================================
# PYTHON LISTS TUTORIAL
# ============================================================================

# ----------------------------------------------------------------------------
# 1. LIST CREATION
# ----------------------------------------------------------------------------
L = ["The bodyguard", 7.0, 1992]

# ----------------------------------------------------------------------------
# 2. LIST INDEXING (POSITIVE AND NEGATIVE)
# ----------------------------------------------------------------------------
print('the same element using negative and positive indexing:\n Postive:', L[0],
      '\n Negative:', L[-3])
print('the same element using negative and positive indexing:\n Postive:', L[1],
      '\n Negative:', L[-2])
print('the same element using negative and positive indexing:\n Postive:', L[2],
      '\n Negative:', L[-1])

# ----------------------------------------------------------------------------
# 3. ADDING ELEMENTS TO LISTS
# ----------------------------------------------------------------------------

# Using extend() - adds elements individually
L = ["The Bodyguard", 7.0]
L.extend(['pop', 10])
print('List after extending:', L)

# Using append() - adds entire object as single element
L = ["The Bodyguard", 7.0]
L.append(['pop', 10])
print('List after appending:', L)

L.append(['a', 'b'])
print('List after appending another list:', L)

# ----------------------------------------------------------------------------
# 4. MODIFYING LIST ELEMENTS
# ----------------------------------------------------------------------------
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
print('The first element is:', A[0])
print('The second element is:', A[1])
print('The third element is:', A[2])

# ----------------------------------------------------------------------------
# 5. DELETING LIST ELEMENTS
# ----------------------------------------------------------------------------
print('Before change:', A)
del(A[0])
print('After change:', A)

# ----------------------------------------------------------------------------
# 6. STRING OPERATIONS
# ----------------------------------------------------------------------------
'hard rock'.split()
print('Split string:', 'hard rock'.split())

# ----------------------------------------------------------------------------
# 7. LIST COPYING AND CLONING
# ----------------------------------------------------------------------------

# Copy by reference (shallow copy)
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone by value (deep copy using slicing)
B = A[:]