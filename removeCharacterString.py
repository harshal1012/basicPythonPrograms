def remove_ith_character(input_string, index):
    if 0 <= index < len(input_string):
        return input_string[:index] + input_string[index + 1:]
    else:
        print(f"Error: Index {index} is out of range for the given string.")
        return input_string

# Example usage:
input_str = "example"
index_to_remove = 3

result = remove_ith_character(input_str, index_to_remove)

print(f"Original String: {input_str}")
print(f"String after removing character at index {index_to_remove}: {result}")
