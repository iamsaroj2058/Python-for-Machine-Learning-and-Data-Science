# Task 02: Ticket Price Calculator Exercise

## Objective
"""Create a program that calculates the ticket price for a movie based on the age and whether the customer is a student.

## Requirements

1. Get the user's age and whether they are a student (True or False) as input.
2. Define the ticket prices:
   - Children (age 0-12): \$10
   - Teenagers (age 13-17): \$15
   - Adults (age 18 and above): $20
   - Students (regardless of age): \$18 (discounted price)
3. Calculate and print the ticket price based on the user's age and student status.
4. Handle cases where the entered age is not a valid numeric value.
5. Provide a message for cases where the age is negative or non-integer."""

# Get user input for age and student status
try:
    age = int(input("Enter your age: "))
    is_student = input("Are you a student? (True/False): ").lower() == 'true'

    # Define ticket prices
    children_price = 10
    teenagers_price = 15
    adults_price = 20
    student_price = 18

    # Check for valid age
    if age < 0 or not isinstance(age, int):
        print("Invalid age. Please enter a valid positive integer.")
    else:
        # Calculate ticket price based on age and student status
        if age <= 12:
            ticket_price = children_price
        elif 13 <= age <= 17:
            ticket_price = teenagers_price
        else:
            ticket_price = student_price if is_student else adults_price

        # Print the ticket price
        print(f'Ticket Price: ${ticket_price}')

except ValueError:
    print("Invalid input. Please enter a valid numeric value for age.")
