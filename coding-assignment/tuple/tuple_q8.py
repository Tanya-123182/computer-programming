#Write a Python program to find the union of two tuples (combine two tuples and remove duplicates).

tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
union_tuple = tuple(set(tuple1) | set(tuple2))
print(union_tuple)  # (1, 2, 3, 4, 5)
