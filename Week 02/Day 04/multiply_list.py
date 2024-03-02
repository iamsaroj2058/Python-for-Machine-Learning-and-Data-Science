# Q.1 Write a python function to multiply all the numbers in a list
def multiply_numbers(numbers):
    """
    Multiply all the numbers in a list.
    """
    result = 1  # Initialize result to 1, as multiplying by 0 would always give 0
    
    for number in numbers:
        result *= number
    
    return result

# Example usage:
numbers_list = [2, 3, 4, 5]
result = multiply_numbers(numbers_list)
print(f"The product of the numbers in the list is: {result}")
