def is_valid_word(word):
    return word.isalpha() and len(word) > 0

def generate_word_pyramid(word, direction='up'):
    if not is_valid_word(word):
        print("Invalid input. Please enter a valid word.")
        return

    length = len(word)

    if direction.lower() == 'up':
        for i in range(length):
            spaces = " " * (length - i - 1)
            pyramid_level = spaces + " ".join(word[:i + 1])
            print(pyramid_level.center(2 * length - 1))
    elif direction.lower() == 'down':
        for i in range(length, 0, -1):
            spaces = " " * (length - i)
            pyramid_level = spaces + " ".join(word[:i])
            print(pyramid_level.center(2 * length - 1))
    else:
        print("Invalid direction. Please choose 'up' or 'down'.")

# User input
user_word = input("Enter a word: ")
pyramid_direction = input("Enter the pyramid direction ('up' or 'down'): ")

# Generate and print the word pyramid
generate_word_pyramid(user_word, pyramid_direction)
