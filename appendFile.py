# Specify the file path
file_path = 'path/to/your/file.txt'

# Input string from the user
user_input = input("Enter a string to append to the file: ")

# Open the file in append mode and write the input string
try:
    with open(file_path, 'a') as file:
        file.write(user_input + '\n')
    print(f"The string has been appended to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
