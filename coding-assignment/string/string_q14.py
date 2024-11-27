#Check if a string is a valid email address:

import re
def is_valid_email(s):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(pattern, s))

print(is_valid_email("example@example.com"))  # True
print(is_valid_email("example.com"))  # False
