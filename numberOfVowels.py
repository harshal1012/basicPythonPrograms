def count_vowels(input_str):
    # Define a set of vowels
    vowels = set("aeiouAEIOU")

    # Count the number of vowels in the input string
    vowel_count = sum(1 for char in input_str if char in vowels)

    return vowel_count

# Example string
my_string = "Hello, World!"

# Call the function and print the result
result = count_vowels(my_string)
print(f"The number of vowels in the string is: {result}")
