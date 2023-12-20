def common_letters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    common_set = set1.intersection(set2)
    common_letters_list = sorted(list(common_set))
    return common_letters_list

# Input strings
input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

# Call the function and print the result
result = common_letters(input_string1, input_string2)

if result:
    print(f"Common letters in the two strings: {', '.join(result)}")
else:
    print("No common letters found.")
