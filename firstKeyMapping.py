def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if the value is not found in the dictionary

# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
target_value = 20

result = find_key_by_value(my_dict, target_value)

if result is not None:
    print(f"The first key mapping to the value {target_value} is: {result}")
else:
    print(f"The value {target_value} is not found in the dictionary.")
