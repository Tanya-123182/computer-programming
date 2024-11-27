#Write a Python program to find the frequency of each character in a string using a dictionary.

my_string = "hello"
freq = {}
for char in my_string:
    freq[char] = freq.get(char, 0) + 1
print(freq)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
