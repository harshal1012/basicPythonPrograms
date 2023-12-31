def generate_list():
    # Function to generate values using the formula 3n² + 4n + 6
    def formula(n):
        return 3 * n**2 + 4 * n + 6

    # Creating a list with 10 members using the formula
    result_list = [formula(n) for n in range(1, 11)]

    return result_list

# Generating and printing the list
result_list = generate_list()
print("Generated List:", result_list)
