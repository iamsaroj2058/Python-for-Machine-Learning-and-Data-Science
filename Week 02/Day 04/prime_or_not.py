# Q.7 Write a Python function that takes a number as a parameter and check the
# number is prime or not.
def is_prime(number):
    """
    Check if a given number is a prime number.
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    # Check for divisors starting from 3 up to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

# Example usage:
user_input = int(input("Enter a number: "))

if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
