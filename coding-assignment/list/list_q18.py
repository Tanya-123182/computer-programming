def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)