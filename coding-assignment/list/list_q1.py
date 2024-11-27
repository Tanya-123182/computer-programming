def second_largest(arr):
    arr = list(set(arr))  # Remove duplicates
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None
