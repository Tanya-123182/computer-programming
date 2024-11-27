#Write a Python program to merge two dictionaries and add values for the common keys.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
for key in dict1:
    if key in dict1 and key in dict2:
        dict1[key] = dict1[key] + dict2[key]
print(dict1)  # {'a': 1, 'b': 5, 'c': 4}
