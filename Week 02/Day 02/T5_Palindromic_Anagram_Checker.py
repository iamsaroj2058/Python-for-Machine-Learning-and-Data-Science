"""# Task 05: Palindromic Anagram Checker

## Objective
Create a program that checks if a given string can be rearranged to form a palindromic string.

## Requirements

1. A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.
2. Ask the user to input a string.
3. Check and print whether the given string can be rearranged to form a palindrome.
4. Ignore spaces and consider the characters in a case-insensitive manner.
5. Handle cases where the input is empty or contains non-alphabetic characters."""

def is_palindromic_anagram(input_str):
    # Check if the input is empty or contains non-alphabetic characters
    if not input_str.isalpha():
        print("Invalid input. Please enter a string containing only alphabetic characters.")
        return False

    # Ignore spaces and consider characters in a case-insensitive manner
    input_str = input_str.replace(" ", "").lower()

    # Count the occurrences of each character
    char_count = {}
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if the string can be rearranged to form a palindrome
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                print("The given string cannot be rearranged to form a palindromic string.")
                return False

    print("The given string can be rearranged to form a palindromic string.")
    return True

if __name__ == "__main__":
    # Ask the user to input a string
    user_input = input("Enter a string: ")

    # Check and print whether the given string can be rearranged to form a palindrome
    is_palindromic_anagram(user_input)
