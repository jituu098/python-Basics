num = int(input('Enter the length of the fibanocci terms you want to be generated : '))
f1= 0
f2 = 1
print(f'f1 = {f1} \n f2= {f2}')
if num == 0:
    print("fabi number cannont be enter as a zero it's already taken")
else:
    for i in range(2, num):
        f3 = f1 + f2
        print(f3, end=" ")
        f1 = f2 
        f2 = f3