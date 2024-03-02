#  Write a python function that takes a list and returns a new list with unique elements of the first list
def unique_elements(input_list):
    """
    Return a new list with unique elements from the given list.
    """
    return list(set(input_list))

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(original_list)

print(f"Original List: {original_list}")
print(f"Unique List: {unique_list}")
