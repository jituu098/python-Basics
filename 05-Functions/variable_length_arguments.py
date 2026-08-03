# * basically indicates that the length of the arguments is variable
def total_marks(name, *marks):
    total = sum(marks)
    average = total/ len(marks)

    print('Name: ',name)
    print('Marks: ', marks)
    print('Total: ', total)
    print('Average: ', average)

total_marks('Jitesh Yadav', 45, 85, 95,80)