def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [4, 2, 9, 7, 5, 1]
target_value = 7

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target value {target_value} found at index {result}")
else:
    print(f"Target value {target_value} not found in the list")
