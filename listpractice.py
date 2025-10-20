fruit_basket = []

fruit_basket.append("apple")
fruit_basket.append("banana")
fruit_basket.append("carrot")

fruit = fruit_basket.pop(0)
print(fruit_basket)
print(fruit)

# using a negative index
my_list = ["apple", "banana", "blueberry"]
print(my_list[-1])

# reversing a list
reverse_list = [2, 4, 6, 0, 1]
reverse_list.reverse()
print(reverse_list)

# slicing a list
slice_list = [2, 4, 6, 0, 1]
sliced_list = slice_list[0:3]
print(sliced_list)
