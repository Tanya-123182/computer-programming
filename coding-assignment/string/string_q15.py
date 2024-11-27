#Replace all occurrences of a substring:

def replace_substring(s, old, new):
    return s.replace(old, new)

print(replace_substring("hello world", "world", "everyone"))  # "hello everyone"
