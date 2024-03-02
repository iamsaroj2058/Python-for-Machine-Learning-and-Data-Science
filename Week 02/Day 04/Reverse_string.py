# Q.2 Write a python function to reverse a string
def reverse_string(input_string):
    """
    Reverse a given string.
    """
    reversed_str = ''.join(reversed(input_string))
    return reversed_str

# Example usage:
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(f"The original string: {original_string}")
print(f"The reversed string: {reversed_string}")
