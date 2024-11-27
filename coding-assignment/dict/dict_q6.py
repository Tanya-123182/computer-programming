#Write a Python program to create a dictionary from two lists (one as keys, the other as values).

keys = ["name", "age", "job"]
values = ["John", 25, "Developer"]
my_dict = dict(zip(keys, values))
print(my_dict)  # {'name': 'John', 'age': 25, 'job': 'Developer'}
