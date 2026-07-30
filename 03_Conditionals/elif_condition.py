# elif parts get executed when the if condition becomes false 
# and matches the elif condition
# if not elif also become false than else part will be executed

# Syntax: 
# if (condition):  # executes when conditon true else goes to elif part
#      body or statement
# elif (condition):  # executes when if condition become false

# executes when above conditions become false
# else:    # executes when elif condition is false
#     statement 

# Q: print input marks belongs to which Grade?

marks = int(input("Enter your marks: "))

if (marks >= 90):
    print("Grade A")
elif (marks >=75):
    print("Grade B")
elif (marks >=50):
    print("Grade C")
else:
    print("fail")