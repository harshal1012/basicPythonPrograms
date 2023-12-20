def is_in_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

# Example usage:
lower_limit = 10
upper_limit = 50

number_to_check = 25
if is_in_range(number_to_check, lower_limit, upper_limit):
    print(f"{number_to_check} is in the range.")
else:
    print(f"{number_to_check} is not in the range.")
