# by default input take input as a strings
name = input("Enter you name: ")
print("Hello", name)

# Integer input
age = int(input("Enter age: "))
print("Age: ", age)

# Float input
height = float(input("Enter height: "))
print("Height: " , height)

#multiple input
name , age = input("Enter your name and age: ").split()
print("Name: ", name)
print("Age: ", age)