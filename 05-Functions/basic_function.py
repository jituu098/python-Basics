# the key word for defining a function is def
# function s with no parameter
def greet():
    print("Hello world")
#calling a function 
greet()

# Parameters - variable written in the function defination
# Arguments - actual values paases to a function

# function with parameter
def greet(name):
    print("Welcome: ", name)
    print("Have a great day")

# calling function and passsing arguments
greet("jitesh")

#Q: Calculate area of rectange using function

def rect_area(length, width):
    area = length * width
    print("Length: ", length)
    print("Width: ", width)
    print("Area : ", area)

# caling and passing a arguments to a function
rect_area(15,6)

# default arguments in a function 
def greet(name, country="India"):
    print("Hello ",name)
    print("Country: ",country)

# if country is not provided it will taka default parameter called india
greet("Jitesh")
print()

greet("John", "USA")