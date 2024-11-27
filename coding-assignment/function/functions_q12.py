#Function to Check for Balanced Parentheses in an Expression

def is_balanced(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    return not stack
