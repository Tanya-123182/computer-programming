#Write a Python program to find the common elements between two tuples.

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
common_elements = tuple(set(tuple1) & set(tuple2))
print(common_elements)  # (3, 4)
