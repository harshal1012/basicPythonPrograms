def count_occurrences(input_str, target_letter):
    # Convert the input string and target letter to lowercase for case-insensitive matching
    input_str_lower = input_str.lower()
    target_letter_lower = target_letter.lower()

    # Count occurrences of the target letter in the string
    occurrences = input_str_lower.count(target_letter_lower)

    return occurrences

# Example string
my_string = "Hello, World!"

# Given letter to count
given_letter = 'o'

# Call the function and print the result
result = count_occurrences(my_string, given_letter)
print(f"The letter '{given_letter}' occurs {result} times in the string.")
