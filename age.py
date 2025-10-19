# Create a program that asks the user to enter their name and their age. Print out a message addressed to them
# that tells them the year that they will turn 100 years old.

age = int(input("Enter your current age: "))
name = input("Enter your name: ")
current_year = 2025

hundredth_year = 100 - age
print(name + "you will turn 100  in " + hundredth_year)
