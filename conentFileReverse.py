# Specify the file path
file_path = 'path/to/your/file.txt'

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the contents of the file
        file_contents = file.read()
        
        # Reverse the contents of the file
        reversed_contents = file_contents[::-1]

        # Print or process the reversed file contents as needed
        print("Reversed File Contents:")
        print(reversed_contents)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
