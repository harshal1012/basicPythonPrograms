# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Given key to remove
given_key = 'age'

# Check if the key exists before removing it
if given_key in my_dict:
    removed_value = my_dict.pop(given_key)
    print(f"Key '{given_key}' with value '{removed_value}' removed.")
else:
    print(f"Key '{given_key}' does not exist in the dictionary.")
    
# Print the updated dictionary
print("Updated Dictionary:", my_dict)
