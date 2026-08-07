# A list is mutable, meaning its elements can be changed.
fruits_list = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits_list)

# Convert the list into a tuple using the tuple() constructor.
# The new tuple contains the same elements as the list.
fruits_tuple = tuple(fruits_list)

print("\nTuple after Conversion:")
print(fruits_tuple)

# Check the data types
print("\nData Types:")
print("List Type :", type(fruits_list))
print("Tuple Type:", type(fruits_tuple))

# Since tuples are immutable, we cannot modify their elements.
# Uncommenting the line below will raise a TypeError.
# fruits_tuple[0] = "Grapes"

# However, the original list is still mutable.
fruits_list.append("Grapes")

print("\nUpdated List:")
print(fruits_list)

print("\nTuple Remains Unchanged:")
print(fruits_tuple)