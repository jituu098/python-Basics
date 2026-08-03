# Indexing in String
# index start from 0 and in string even a white space also counted as a index
# each char can be access through indexing
language = "Python"

print("First character:", language[0])
print("Third character:", language[2])
print("Last character:", language[-1])
print("Second last character:", language[-2])


# String_slicing
# Slicing is creating new string from the previous string
# Syntax
# string_varible[start_index: end_index]
# it will give a new string and excludes the last index char

text = "Python Programming"

print("Original:", text)
print("First 6 characters:", text[:6])
print("Programming:", text[7:])
print("Every second character:", text[::2])
print("Reversed string:", text[::-1])