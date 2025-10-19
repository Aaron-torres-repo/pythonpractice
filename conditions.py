# ticket pricing. under 18 entry is free. student or over 65 - 50% off. everyone else pays full price
age = input("Enter age: ")
student = input("Are you a student?: ")

if age > "65" or student == "yes":
    print("Ticket is 50% off")
    if age < "18":
        print("Entry is free")
else:
    print("You have to pay full price")
