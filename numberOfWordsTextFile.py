def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            line_count = content.count('\n') + 1  # Assuming the last line does not end with a newline character

            return word_count, line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = 'sample_text_file.txt'  # Replace with the path to your text file

result = count_words_and_lines(file_path)

if result is not None:
    word_count, line_count = result
    print(f"Number of words: {word_count}")
    print(f"Number of lines: {line_count}")
