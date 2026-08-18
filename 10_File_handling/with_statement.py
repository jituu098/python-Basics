# Using with statement
# The with statement automatically closes
# the file after the block is completed.
# Therefore, file.close() is not required.

with open("student.txt", "w") as file:
    file.write("Name: Jitesh\n")
    file.write("Course: Python\n")
    file.write("Topic: File Handling\n")

print("Data written successfully.")

# Reading the file using the with statement
with open("student.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)