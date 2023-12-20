def letters_in_first_not_in_second(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    letters_not_in_second = sorted(list(set1 - set2))
    return letters_not_in_second

# Input strings
input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

# Call the function and print the result
result = letters_in_first_not_in_second(input_string1, input_string2)

if result:
    print(f"Letters in the first string but not in the second: {', '.join(result)}")
else:
    print("No letters found in the first string but not in the second.")
