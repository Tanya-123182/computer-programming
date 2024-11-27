#Write a Python program to find the difference between two tuples.

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
diff_elements = tuple(set(tuple1) - set(tuple2))
print(diff_elements)  # (1, 2)
