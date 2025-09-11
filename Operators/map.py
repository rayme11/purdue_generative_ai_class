# Define a function to square a number
def square(x):
    return x * x        
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
# Use map() to apply the square function to each number in the list
squared_numbers = list(map(square, numbers))
# Print the result
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
