numbers = [10, 20, 30, 40, 50, 60, 70]

print("Original List:", numbers)

# slicing is simply making a new list from the old list
# Syntax list[start_index: end_index]
# it will make the new list from the start and end index till which you want to take
# it doesn't include the last element

# in this it will print from the o index to 2 index
print("First 3 Elements:", numbers[:3])

# indexing through negative index
# accsing of items from the last 
print("Last 3 Elements:", numbers[-3:])

print("Every Second Element:", numbers[::2])

# it i will reverse the list items 
print("Reverse List:", numbers[::-1])