# Sytnax:
# if(condition):  # executes when if conditon is true if become false it will goes to else
#     if(codition):
#         # statement
#     elif:(condition):
#         # statement
#     else:
#         #statement
# else:
#     # statement

#Q:if a person have the citizensip and age >= 18 than he/she eligible to vote
citizen = input("Do you have a citizenship?: ")
age = int(input("Enter your age: "))
if age >=18:
    if(citizen == "yes"):
        print("Eligible to vote: ")
    else:
        print("Not eligible becaue you are not citizen: ")
else:
    print("Not eligible because you are under 18")