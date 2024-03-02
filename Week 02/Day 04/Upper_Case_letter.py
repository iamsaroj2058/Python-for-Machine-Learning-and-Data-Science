# Write a python function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case_letters(input_string):
    """
    Count the number of uppercase and lowercase letters in a given string.
    """
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
user_input = input("Enter a string: ")
upper, lower = count_case_letters(user_input)

print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")
