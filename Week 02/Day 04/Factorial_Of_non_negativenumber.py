# Write a python function to find factorial of a given non negativenumber
def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage:
number = int(input("Enter a non-negative integer: "))
result = factorial(number)

print(f"The factorial of {number} is: {result}")