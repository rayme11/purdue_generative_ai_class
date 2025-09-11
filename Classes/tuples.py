mixed_tuple = (42, "Hello", 3.14, True) 
print("Mixed Tuple:", mixed_tuple)
# Access elements
print("First Element:", mixed_tuple[0])
print("Second Element:", mixed_tuple[1])
print("Third Element:", mixed_tuple[2])
print("Fourth Element:", mixed_tuple[3])    

# Tuple unpacking
num, text, pi, boolean = mixed_tuple
print("Unpacked Values:")
print("Number:", num)
print("Text:", text)
print("Pi:", pi)
print("Boolean:", boolean)  

# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6, (7, 8)))
print("Nested Tuple:", nested_tuple)

# Accessing elements in nested tuples
print("Element from Nested Tuple:", nested_tuple[2][1])  # Accessing 4
print("Element from Nested Tuple:", nested_tuple[3][2][0])  # Accessing 7       

# Tuple methods
sample_tuple = (10, 20, 30, 20, 40, 20)
print("Count of 20 in Sample Tuple:", sample_tuple.count(20))
print("Index of 30 in Sample Tuple:", sample_tuple.index(30))   

# Immutability demonstration
try:
    sample_tuple[1] = 25  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be changed.")

# Concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 3
print("Concatenated Tuple:", concatenated_tuple)
print("Repeated Tuple:", repeated_tuple)

# Length of tuple
print("Length of Mixed Tuple:", len(mixed_tuple))       

# Slicing
print("Sliced Tuple (first 3 elements):", mixed_tuple[:3])
print("Sliced Tuple (last 2 elements):", mixed_tuple[-2:])  

# Iterating through a tuple
print("Iterating through Mixed Tuple:")
for item in mixed_tuple:
    print(item)
# Tuple with single element
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)
print("Type of Single Element Tuple:", type(single_element_tuple))      
# Converting list to tuple
sample_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(sample_list)
print("Converted Tuple from List:", converted_tuple)
# Converting tuple to list
converted_list = list(mixed_tuple)
print("Converted List from Tuple:", converted_list)
# Using tuples as dictionary keys
tuple_key_dict = {('a', 1): "Value1", ('b', 2): "Value2"}
print("Dictionary with Tuple Keys:", tuple_key_dict)
print("Accessing Value with Tuple Key ('a', 1):", tuple_key_dict[('a', 1)])
# Nested tuple unpacking
nested_unpacking_tuple = (1, (2, 3), (4, (5, 6)))
a, (b, c), (d, (e, f)) = nested_unpacking_tuple
print("Nested Unpacked Values:", a, b, c, d, e, f)
# Tuple comprehension (using generator expression)
squared_tuple = tuple(x**2 for x in range(5))
print("Squared Tuple using Comprehension:", squared_tuple)
# Demonstrating immutability with concatenation
original_tuple = (1, 2, 3)
new_tuple = original_tuple + (4, 5)
print("Original Tuple after Concatenation Attempt:", original_tuple)
print("New Tuple after Concatenation:", new_tuple)