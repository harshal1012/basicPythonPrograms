def reverse_number_recursive(number):
    # Base case: if the number has only one digit, return the number itself
    if number < 10:
        return number
    # Recursive case: reverse the rest of the number and concatenate the last digit at the beginning
    else:
        last_digit = number % 10
        remaining_digits = number // 10
        reversed_remaining = reverse_number_recursive(remaining_digits)
        return int(str(last_digit) + str(reversed_remaining))

# Example number
my_number = 12345

# Call the function and print the result
result = reverse_number_recursive(my_number)
print(f"The reversed number is: {result}")
