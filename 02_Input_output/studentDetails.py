name = input('Enter the name of the student: ')
usn = input('Enter the USN : ')
marks1 = float(input('Enter the marks of Math: '))
marks2 = float(input('Enter teh marks of Python: '))
marks3 = float(input('Enter the marks of AI : '))

total = marks1 + marks2 + marks3
percentage = total/3
print("=====STUDENT DETAILS========")
print(f"NAME : {name}")
print(f"USN: {usn}")
print('Marks')
print(f'Math:{marks1} \nPython: {marks2} \nAI : {marks3}')
print(f'Total Marks : {total}')
print(f'Percentage : {percentage:.2f}')