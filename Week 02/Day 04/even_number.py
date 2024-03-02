#  Write a python function to print the even numbers from a given list.
def print_even_numbers(input_list):
    """
    Print the even numbers from a given list.
    """
    even_numbers = [num for num in input_list if num % 2 == 0]
    
    if even_numbers:
        print("Even numbers in the list:", even_numbers)
    else:
        print("No even numbers in the list.")

# Example usage:
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(user_list)
