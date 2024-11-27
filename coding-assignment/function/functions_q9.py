#Function to Find the Missing Number in an Array of Consecutive Numbers

def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum
