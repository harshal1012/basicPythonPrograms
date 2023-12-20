def linear_search(search_list, target):
    for i, item in enumerate(search_list):
        if item == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [1, 5, 7, 9, 12, 15, 19, 21]
target_element = 15

result = linear_search(my_list, target_element)

if result != -1:
    print(f"The target element {target_element} is found at index {result}.")
else:
    print(f"The target element {target_element} is not found in the list.")
