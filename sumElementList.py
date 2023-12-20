def recursive_sum(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: add the first element to the sum of the rest of the list
    else:
        return lst[0] + recursive_sum(lst[1:])

# Example list
my_list = [1, 2, 3, 4, 5]

# Call the function and print the result
result = recursive_sum(my_list)
print(f"The sum of elements in the list is: {result}")
