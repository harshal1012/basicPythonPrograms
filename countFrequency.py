def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through each character in the string
    for char in input_string:
        # Increment the frequency count for the current character
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

# Example usage:
input_str = "hello world"
result = count_character_frequency(input_str)

# Display the character frequencies
for char, frequency in result.items():
    print(f"Character '{char}' appears {frequency} times in the string.")
