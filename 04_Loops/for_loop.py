# Q: Print numbers from 1 to 5 using a for loop 

for i in range(1,6):
    print(i)

# print only the even number between the 1 and 20
# last number 20 will be not included it will execue till 19 only
#last - 1 
for i in range(1,20):
    if (i %2 ==0):
        print(i, end = " ")  # skip number when i == 8 
print()

# break statement in for loop
# it will print till 7 and when it reaches to 8 than break statement break the loop comes out of the loop 
for i in range(1, 10):
    if (i == 8): # comes out of the loop when i == 8 
        break
    print(i, end= " ") # end is used to print the number in same line 
print()

# continue statement in for loop 
# simply it skip that number and move ahead in the loop
# it will skip when it i reaches 8 it will skip that number and continue to execute
for i in range(1, 10):
    if (i == 8): 
        continue
    print(i , end= " ")