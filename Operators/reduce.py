from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Define a function to sum two numbers
def add(x, y):
    return x + y

# Use reduce() to apply the add function cumulatively to the items in the list
sum_of_numbers = reduce(add, numbers)
# Print the result
print("Sum of numbers:", sum_of_numbers)  # Output: Sum of numbers: 15  
# You can also use a lambda function with reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)  # Output: Product of numbers: