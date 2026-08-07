# Tuples have only two built-in methods:
# Since tuples are not mutable hence they don't have method like append ,insert etc.
# 1. count()
# 2. index()

numbers = (10, 20, 30, 20, 40, 20, 50)

print("Original Tuple:")
print(numbers)

# count() method returns how many times a value appears
count_20 = numbers.count(20)

print("\nNumber 20 appears", count_20, "times.")

# index() method returns the first occurrence of a value
position = numbers.index(40)

print("40 is present at index:", position)

# Using len() to get the total number of elements
print("\nTotal Elements:", len(numbers))

# Membership operator
# it returns a boolean values 
# if 30 present in the tuple then it returns True and if not present than False like this it works
print("Is 30 present?", 30 in numbers)
print("Is 100 present?", 100 in numbers)