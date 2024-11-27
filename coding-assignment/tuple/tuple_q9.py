#Write a Python program to find the index of the maximum and minimum element in a tuple.

my_tuple = (10, 20, 4, 45, 99)
max_index = my_tuple.index(max(my_tuple))
min_index = my_tuple.index(min(my_tuple))
print(f"Max Index: {max_index}, Min Index: {min_index}")
# Max Index: 4, Min Index: 2
