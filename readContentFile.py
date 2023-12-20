file_path = 'path/to/your/file.txt'


try:
    with open(file_path, 'r') as file:
        
        file_contents = file.read()
        
        print("File Contents:")
        print(file_contents)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
