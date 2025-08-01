# ============================================================================
# SHOPPING LIST MANAGEMENT SCENARIO
# ============================================================================

# ----------------------------------------------------------------------------
# TASK 1: LIST INITIALIZATION
# ----------------------------------------------------------------------------
# Create an empty list
Shopping_list = []

# ----------------------------------------------------------------------------
# TASK 2: ADDING ITEMS TO THE LIST
# ----------------------------------------------------------------------------
# Store multiple items to the shopping_list
# Items: Watch, Laptop, Shoes, Pen, Clothes
Shopping_list.extend(['Watch', 'Laptop', 'Shoes', 'Pen', 'Clothes'])

# ----------------------------------------------------------------------------
# TASK 3: LIST ACCESS AND DISPLAY
# ----------------------------------------------------------------------------
# Print First item from the shopping_list
print("First item in the shopping list:", Shopping_list[0])

# Print Last item from the shopping_list
print("Last item in the shopping list:", Shopping_list[-1])

# Print the entire Shopping List
print("Complete Shopping List:", Shopping_list)

# ----------------------------------------------------------------------------
# TASK 4: LIST SLICING
# ----------------------------------------------------------------------------
# Print the items that are important to buy from the Shopping List
# Print "Laptop" and "Shoes" (indices 1 and 2)
print("Important items to buy:", Shopping_list[1:3])

# ----------------------------------------------------------------------------
# TASK 5: MODIFYING LIST ELEMENTS
# ----------------------------------------------------------------------------
# Change the item from the shopping_list
# Instead of "Pen" I want to buy "Notebook" - change item at index 3
Shopping_list[3] = 'Notebook'
print("Updated Shopping List:", Shopping_list)

# ----------------------------------------------------------------------------
# TASK 6: DELETING LIST ELEMENTS
# ----------------------------------------------------------------------------
# Delete the item from the shopping_list that is not required
del(Shopping_list[4])

# Print the final shopping list
print("Shopping List after deletion:", Shopping_list)