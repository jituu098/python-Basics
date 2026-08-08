student = {
    "name": "Jitesh",
    "age": 20,
    "course": "Python",
    "marks": 85
}

# keys() mathod returns all the keys in the dictionary.
print("Keys:")
print(student.keys())

# values() method returns all the values.
print("\nValues:")
print(student.values())

# items() returns key-value pairs.
print("\nItems:")
print(student.items())

# get() safely returns the value of a key.
# It returns None if the key does not exist.
print("\nCourse:", student.get("course"))
print("City:", student.get("city"))

# update() adds new data or modifies existing data.
student.update({"marks": 92, "city": "Bangalore"})

print("\nAfter update():")
print(student)

# pop() removes a key-value pair.
student.pop("age")

print("\nAfter removing age:")
print(student)

# popitem() removes the last inserted key-value pair.
student.popitem()

print("\nAfter popitem():")
print(student)