# write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
# Cost in price (in RS)
# > 100000 15%
# > 50000 and <= 100000 10%
# <= 50000 5%

bike_cost = int(input("Enter cost of bike: "))
if bike_cost > 100000:
    print("15%")
if bike_cost > 50000 and bike_cost <= 100000:
    print("10%")
if bike_cost <= 50000:
    print("5%")
