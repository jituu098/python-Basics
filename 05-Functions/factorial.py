# example of recursion 
# calling a function itself inside a function again and againis called recursion
def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)
num = 5
print(f"Factorial of {num} is {factorial(num)}")