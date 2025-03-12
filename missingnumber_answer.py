def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

# Example usage
arr = [1, 2, 4, 5, 6]  # n should be 6
n = 6
print("Missing number:", find_missing_number(arr, n))