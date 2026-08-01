# Q: Print numbers from 1 to 5 using a while loop
# while loop used when you don't basically how many iteration to do 

# count = 1
# while count <= 5: # it will iterate util the condtion becomes false 
#     print(count)
#     count += 1

# using break statement in while loop
count = 1
while count <= 10:
    if count == 5: 
        count +=1
        continue # it will skip when count == 5
    print(count)
    count += 1
    if count == 8 :
        break # breaks while loop when count ==8        