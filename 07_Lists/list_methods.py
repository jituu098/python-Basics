students = ["Rahul", "Aman", "Priya"]

#list.append() method append the new item in a list at last index 
students.append("Jitesh")

# list.insert() method instert a new item to list at specific postion or index of the list
# Synatx list.instert(index, 'item_name')
students.insert(1, "Riya")

# list.remove() method remove the specific items from the list 
students.remove("Aman")

# list.sort() method sort the list 
students.sort()

print("Students:", students)

# gives the len(list) gives the length of the list
print("Total Students:", len(students))

# it will remove the random items from the list
students.pop()

print("After Pop:", students)