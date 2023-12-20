def is_palindrome(input_str):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in input_str if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example string
my_string = "A man, a plan, a canal, Panama!"

# Call the function and print the result
if is_palindrome(my_string):
    print(f"The string '{my_string}' is a palindrome.")
else:
    print(f"The string '{my_string}' is not a palindrome.")
