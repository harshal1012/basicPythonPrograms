def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to count vowels
result = count_vowels(user_input)

# Display the result
print(f"The number of vowels in the entered string is: {result}")
