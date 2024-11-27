#Write a Python program to convert a dictionary of lists into a dictionary of tuples.

my_dict = {"a": [1, 2, 3], "b": [4, 5, 6]}
dict_of_tuples = {key: tuple(value) for key, value in my_dict.items()}
print(dict_of_tuples)  # {'a': (1, 2, 3), 'b': (4, 5, 6)}
