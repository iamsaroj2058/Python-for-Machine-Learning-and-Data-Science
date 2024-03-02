def is_valid_positive_integer(num):
    try:
        n = int(num)
        return n > 0
    except ValueError:
        return False

def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# Main program
while True:
    # User input and validation
    user_input = input("Enter a positive integer (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    if not is_valid_positive_integer(user_input):
        print("Invalid input. Please enter a valid positive integer.")
        continue

    # Calculate and print prime factorization
    number = int(user_input)
    factors = prime_factorization(number)
    print(f"Prime Factorization of {number}: {factors}")
