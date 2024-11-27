#Write a Python program to count the occurrences of each word in a sentence using a dictionary.

sentence = "hello world hello python"
word_count = {}
words = sentence.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'hello': 2, 'world': 1, 'python': 1}
