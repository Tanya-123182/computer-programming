#Write a Python program to remove an item from a tuple (by converting to a list first).

my_tuple = (1, 2, 3, 4)
temp_list = list(my_tuple)
temp_list.remove(3)
my_tuple = tuple(temp_list)
print(my_tuple)  # (1, 2, 4)
