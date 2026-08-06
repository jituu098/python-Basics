import math
n = int(input("enter the total no of number : "))
numbers = []
total = 0
for i in range(n):
    nums = int(input('Enter the numbers: '))
    numbers.append(nums)
    total += nums

mean = total/n
total = 0
for i in range(n):
    a = (numbers[i] - mean) * (numbers[i] - mean)
    total += a

variance =(total/n)
sd = math.sqrt(variance)

print(f'Total = {total}')
print(f'Mean = {mean}')
print(f"Varience = {variance}")
print(f'standard deviation = {sd}')