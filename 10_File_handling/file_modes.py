# Creating a File 
# The open() function can create a new file.
# "x" mode creates the file only if it does not already exist.

file = open("student.txt", "x")
print("File created successfully.")
# close() releases the file from the program.
file.close()


# writing a file
# "w" mode is used to write data to a file.
# If the file does not exist, Python creates it.
# If the file already exists, its previous content is replaced.
file = open("student.txt", "w")
file.write("Name: Jitesh\n")
file.write("Course: Python\n")
file.write("Age: 20\n")
print("Data written successfully.")
file.close()

# Reading a File
# "r" mode is used to read an existing file.
# The file must already exist.
file = open("student.txt", "r")
# read() reads the complete content of the file.
content = file.read()
print("File Content:")
print(content)
file.close()

# Append mode
# "a" mode adds new data at the end of the file.
# Existing content is not deleted.
file = open("student.txt", "a")
file.write("City: Bangalore\n")
file.write("Language: Python\n")
print("Data appended successfully.")
file.close()