# Syantax:
# if (condition True): // executes when conditon true else goes to else part
#      body or statement
# else:    // executes when if condition is false
#     statement 

# Q: eligble for vote if age greater than or equal 18
age = int(input("Enter your age: "))
if (age >= 18):
    print("You are eligble for vote")

#Q: check the given number is odd or even

number = int(input("Enter a number : "))

if (number % 2 == 0):
    print(number, "is Even number")
else:        # runs when if conditions become Fasle
    print(number, "is Odd number")