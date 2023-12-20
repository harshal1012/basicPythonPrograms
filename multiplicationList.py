def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

# Example list
my_list = [2, 3, 4, 5]

# Call the function and print the result
result = multiply_list(my_list)
print(f"The result of multiplying all items in the list is: {result}")
