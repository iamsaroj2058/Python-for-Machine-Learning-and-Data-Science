def is_valid_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def odd_even_sorter(user_input, order='ascending'):
    numbers = [float(num.strip()) for num in user_input.split(',') if is_valid_number(num)]

    if order.lower() == 'ascending':
        odd_numbers = sorted([num for num in numbers if num % 2 != 0])
        even_numbers = sorted([num for num in numbers if num % 2 == 0])
    elif order.lower() == 'descending':
        odd_numbers = sorted([num for num in numbers if num % 2 != 0], reverse=True)
        even_numbers = sorted([num for num in numbers if num % 2 == 0], reverse=True)
    else:
        print("Invalid order. Please choose 'ascending' or 'descending'.")
        return

    print("Odd Numbers:", odd_numbers)
    print("Even Numbers:", even_numbers)

# User input
user_numbers = input("Enter a list of numbers (comma-separated): ")
sort_order = input("Enter the sort order ('ascending' or 'descending'): ")

# Sort and display the odd and even lists
odd_even_sorter(user_numbers, sort_order)
