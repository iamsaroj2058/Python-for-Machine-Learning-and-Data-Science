"""Create a simple grading system where a student's score is entered, and the program determines the corresponding grade.

## Requirements

1. Get the student's score as input.
2. Use the following grading scale:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
3. Print the grade based on the input score."""
# 4. Handle cases where the entered score is not within the valid range (0-100).


number1=int(input("Enter the grade you get:"))
if 90>=100:
  print("you secure Grade A")
elif 80>=89:
  print("you secure Grade B")
elif 70>=79:
  print("you secure Grade C")
elif 60>=69:
  print("you secure grade D")
else:
  print("you are fail")