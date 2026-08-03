# when condition matches it will return the value
# after matching function return value and break the function no further execution
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

student_marks = 82

grade = calculate_grade(student_marks)

print("Marks:", student_marks)
print("Grade:", grade)