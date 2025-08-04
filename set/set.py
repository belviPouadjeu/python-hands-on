# ----- 1. Remove duplicates by converting a list to a set -----
genres_list = ['rap', 'house', 'electronic music', 'rap']
genres_set = set(genres_list)
print("Unique genres:", genres_set)


# ----- 2. Compare sum of list vs set -----
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])  # Duplicates removed → B = {1, 2}

sum_A = sum(A)  # 1 + 2 + 2 + 1 = 6
sum_B = sum(B)  # 1 + 2 = 3

print("Sum of A:", sum_A)
print("Sum of B:", sum_B)
print("Are the sums equal?", sum_A == sum_B)  # False


# ----- 3. Set union example -----
album_set1 = set(["Thriller", "AC/DC", "Back in Black"])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Union combines both sets, removing duplicates
album_set3 = album_set1.union(album_set2)
print("Union of album sets:", album_set3)

# Check if album_set1 is a subset of album_set3
is_subset = album_set1.issubset(album_set3)
print("Is album_set1 a subset of album_set3?", is_subset)
