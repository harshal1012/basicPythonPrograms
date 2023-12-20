def print_multiplication_table(number, table_range):
    print(f"Multiplication table for {number}:")

    for i in range(1, table_range + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage:
input_number = int(input("Enter a number: "))
table_range = int(input("Enter the range for the multiplication table: "))

print_multiplication_table(input_number, table_range)
