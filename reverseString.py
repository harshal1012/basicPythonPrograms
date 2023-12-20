def reverse_string_recursive(input_str):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(input_str) <= 1:
        return input_str
    # Recursive case: reverse the rest of the string and concatenate the first character at the end
    else:
        return reverse_string_recursive(input_str[1:]) + input_str[0]

# Example string
my_string = "Hello, World!"

# Call the function and print the result
result = reverse_string_recursive(my_string)
print(f"The reversed string is: {result}")
