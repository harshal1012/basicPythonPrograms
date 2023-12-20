# Create a list of tuples with the first element as the number and second element as the square
numbers = [1, 2, 3, 4, 5]

# Using list comprehension to create the list of tuples
tuples_list = [(num, num**2) for num in numbers]

# Print the list of tuples
print("List of Tuples:", tuples_list)
