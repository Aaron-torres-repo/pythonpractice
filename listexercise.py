# todo: get the top 3 shopping expenses
# the result should be [250, 160, 92]

shopping_expense = [24, 60, 8, 92, 160, 80, 250, 20, 10]

# this creates a copy of the list, so we aren't alternating original list
shopping_expense_copy = shopping_expense[:]
print(shopping_expense_copy)
# this sorts the list from lowest to highest values
shopping_expense_copy.sort()
print(shopping_expense_copy)
# then I reversed it to list it from highest to lowest
shopping_expense_copy.reverse()
print(shopping_expense_copy)
# then I just indexed the first 3
top_3_expenses = shopping_expense_copy[:3]
print(top_3_expenses)
