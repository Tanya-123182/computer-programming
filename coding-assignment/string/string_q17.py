#Find the longest word in a string:

def longest_word(s):
    words = s.split()
    return max(words, key=len)

print(longest_word("The quick brown fox"))  
