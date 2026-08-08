# A dictionary stores data in key-value pairs.
# Each key must be unique.
# as lists are accessed by the index 
# dictionay value accessed by the keys 
student = {
    "name": "Jitesh",
    "age": 20,
    "course": "Python",
    "marks": 85
}

print("Student Dictionary:")
print(student)

# Accessing values using their keys
print("\nStudent Name:", student["name"])
print("Student Age:", student["age"])
print("Student Marks:", student["marks"])

# Adding a new key-value pair
student["city"] = "Bangalore"

print("\nAfter Adding City:")
print(student)

# Updating an existing value
student["marks"] = 90

print("\nAfter Updating Marks:")
print(student)