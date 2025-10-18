# Write a program to accept percentage from the user and display the grade according to the following criteria:
# Marks
# > 90 == A
# > 80 and <= 90 == B
# =60 and <= 80 == C
# below 60 == D

grade = int(input("Enter grade: "))
if grade >= 90:
    print("A")
if grade > 80 and grade <= 89:
    print("B")
if grade > 70 and grade <= 79:
    print("C")
if grade > 60 and grade <= 69:
    print("D")
