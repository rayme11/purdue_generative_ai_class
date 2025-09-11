# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use filter() to apply the is_even function to each number in the list
even_numbers = list(filter(is_even, numbers))

# Print the result
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
