#Write a Python program to merge two dictionaries into one.

dict1 = {"name": "John", "age": 25}
dict2 = {"address": "New York", "job": "Developer"}
dict1.update(dict2)
print(dict1)  # {'name': 'John', 'age': 25, 'address': 'New York', 'job': 'Developer'}
