import copy

# Original nested list
spam = [1, 2, [3, 5], 4]

print("Original List:")
print(spam)

#Shallow Copy
# copy.copy() creates a new outer list, but the nested list
# is still shared between the original and the copied list.

print("\nAfter modifying using shallow copy:")

cheese = copy.copy(spam)

# Modifying the nested list
cheese[2][1] = 7

# Both lists are affected because the nested list is shared.
print("Original List:", spam)
print("Shallow Copy :", cheese)

# Deep Copy 
# copy.deepcopy() creates a completely independent copy,
# including all nested lists.

print("\nAfter modifying using deep copy:")

cheese = copy.deepcopy(spam)

# Modifying the nested list in the deep copy
cheese[2][1] = 10

# Only the copied list changes.
print("Original List:", spam)
print("Deep Copy    :", cheese)