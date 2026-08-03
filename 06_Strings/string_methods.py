text = "  python programming  "

print("Original:", text)

# .upper() method convert all the lowerCase letter present in the string to a Upper case
print("Upper:", text.upper())

# .lower() method convert all the upperCase letter present in the string to a Lower caseC
print("Lower:", text.lower())

# .Title() method convert all the lowerCase letter of every word into a uppercase  # eg - the movies = The Movie
print("Title:", text.title())

# .strip() method remove all the extra white spaces and the escape character 
print("Strip:", text.strip())

# .repalce() method as a name it will replace the string eg given "python" to "java"
print("Replace:", text.replace("python", "Java"))

# .count() method count all the letter of "m" present in the string
print("Count of 'm':", text.count("m"))

# .startswith() method check whether the given string string with the word python or not it gives a boolean value (i.e True or False)
print("Starts with 'python':", text.strip().startswith("python"))