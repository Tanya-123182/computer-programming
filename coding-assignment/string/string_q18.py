#Find the last occurrence of a substring in a string:

def last_occurrence(s, substring):
    return s.rfind(substring)

print(last_occurrence("hello world", "o"))  # 7
