def append_items(source_list, target_list):
    # Using extend() method
    target_list.extend(source_list)
    # Alternatively, you can use the + operator
    # target_list += source_list

# Example usage:
source_list = [1, 2, 3]
target_list = [4, 5, 6]

append_items(source_list, target_list)

print("Source List:", source_list)
print("Target List after appending:", target_list)
