#Find the first occurrence of a substring in a string:

def first_occurrence(s, substring):
    return s.find(substring)

print(first_occurrence("hello world", "world"))  # 6
