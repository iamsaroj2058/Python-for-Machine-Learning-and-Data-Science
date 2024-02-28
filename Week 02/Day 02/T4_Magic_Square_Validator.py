# Task 04: Magic Square Validator

## Objective
"""Create a program that checks if a given 3x3 matrix forms a magic square.

## Requirements

1. A magic square is a square matrix where the sums of the numbers in each row, column, and both main diagonals are the same.
2. Ask the user to input a 3x3 matrix (nine integer values).
3. Check and print whether the given matrix forms a magic square.
4. Handle cases where the input matrix is not of size 3x3 or contains non-integer values."""

def is_magic_square(matrix):
    # Check if the matrix is 3x3
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        return False
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check rows, columns, and diagonals
    for i in range(3):
        if sum(matrix[i]) != target_sum or sum(matrix[j][i] for j in range(3)) != target_sum:
            return False
    
    if sum(matrix[i][i] for i in range(3)) != target_sum or sum(matrix[i][2-i] for i in range(3)) != target_sum:
        return False
    
    return True

def get_matrix_from_user():
    # Get user input for the matrix
    matrix = []
    for i in range(3):
        row = input(f"Enter the values for row {i + 1} (separated by space): ").split()
        try:
            row = [int(value) for value in row]
        except ValueError:
            print("Invalid input. Please enter integer values.")
            return None
        matrix.append(row)
    
    return matrix

if __name__ == "__main__":
    # Step 2: Ask the user to input a 3x3 matrix
    user_matrix = get_matrix_from_user()

    if user_matrix is not None:
        # Step 3: Check and print whether the given matrix forms a magic square
        if is_magic_square(user_matrix):
            print("The given matrix forms a magic square.")
        else:
            print("The given matrix does not form a magic square.")
