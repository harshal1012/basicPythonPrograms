def check_element_in_tuple(element, my_tuple):
    if element in my_tuple:
        return True
    else:
        return False

# Example usage:
my_tuple = (1, 2, 3, 4, 5)

element_to_check = 3
if check_element_in_tuple(element_to_check, my_tuple):
    print(f"{element_to_check} exists in the tuple.")
else:
    print(f"{element_to_check} does not exist in the tuple.")
