
principal = 240000
annual_rate = 0.05
years = 2

time_compound = 12*2
# calculate interest earned
# expected result is 264600.0

compound_interest = (1 + annual_rate)**years
final_result = principal*compound_interest
print(final_result.__round__())
