import random

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Additional Challenge: Allow the user to choose the range
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))
    
    # Generate a random number within the specified range
    secret_number = random.randint(lower_limit, upper_limit)

    attempts = 0

    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
number_guessing_game()
