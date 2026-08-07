# A tuple is an ordered collection of items.
# Tuples are immutable, which means their values
# cannot be changed after creation.

# Creating a tuple of fruits
# as lista are inside the sqaure braces similarly tuples are inside parenthesis
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits Tuple:")
print(fruits)

# Accessing tuple elements using indexing
print("\nFirst Fruit:", fruits[0])
print("Last Fruit :", fruits[-1])

# A tuple can store different data types
student = ("Jitesh", 20, "Python", True)

print("\nStudent Information:")
print(student)

# Creating a tuple with a single element
# A comma is mandatory; otherwise Python
# treats it as a normal value.
single_value = (100,)

print("\nSingle Element Tuple:")
print(single_value)

# Creating an empty tuple
empty_tuple = ()

print("\nEmpty Tuple:")
print(empty_tuple)