def is_substring_present(main_string, substring):
    return substring in main_string

# Example usage:
main_string = "Hello, how are you today?"
substring_to_check = "how are"

if is_substring_present(main_string, substring_to_check):
    print(f"The substring '{substring_to_check}' is present in the main string.")
else:
    print(f"The substring '{substring_to_check}' is not present in the main string.")
