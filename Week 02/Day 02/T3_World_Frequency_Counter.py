''' Task 03: Word Frequency Counter

 Objective
Create a program that analyzes a given text and counts the frequency of each unique word.

## Requirements

1. Ask the user to input a paragraph or sentence.
2. Tokenize the input into words (ignoring punctuation and case sensitivity).
3. Count the frequency of each unique word.
4. Display the word frequencies in alphabetical order.
5. Handle cases where the input is empty.'''

import string

# Step 1: Ask the user to input a paragraph or sentence
user_input = input("Enter a paragraph or sentence: ")

# Step 5: Handle cases where the input is empty
if not user_input:
    print("Input is empty. Exiting.")
else:
    # Step 2: Tokenize the input into words (ignoring punctuation and case sensitivity)
    words = [word.strip(string.punctuation).lower() for word in user_input.split()]

    # Step 3: Count the frequency of each unique word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Step 4: Display the word frequencies in alphabetical order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[0])

    print("Word Frequencies:")
    for word, frequency in sorted_word_count:        
        print(f"{word}: {frequency}")
