name = "Jitesh"
age = 20
language = "Python"


# f-string uses and f before start of string and under shich every values write int eh curly braces{} 
# directly value inserted using curoly braces
print("Using f-string:")
print(f"My name is {name}. I am {age} years old and learning {language}.")

# in this we left empty curly braces and and use .forma() by giving variables and it will print respectively 
print("\nUsing format():")
print("My name is {}. I am {} years old.".format(name, age))

# uses %d for the integer %f float and %s for string and give values under % with parenthesis
# print values respectively
print("\nUsing % operator:")
print("My name is %s and I am %d years old." % (name, age))



# Escape characters
# used for the next line in the string or for tab spaces
# \n use to create a new line
#\t use to create tab space betwen string
## also used in the single and double string

# print hello in one one and creates a new line to print world
print("Hello\nWorld")

# makes a spaces equal to one tab
print("Python\tProgramming")

# for keeping "python is awesome" in double quotes inside double quotes string
# we use backslash
print("She said, \"Python is awesome!\"")

print('It\'s a beautiful day.')

# for directory it will count one backslash where as other behave as a escape characters
print("C:\\Users\\Jitesh\\Documents")