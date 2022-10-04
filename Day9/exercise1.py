#Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


def convertToGrade(n,value):
    if n > 90:
        value = "Outstanding"
    elif n >= 81 and n <= 90:
        value = "Exceeds Expectations"
    elif n >= 71 and n <= 80:
        value = "Acceptable"
    elif n >= 70:
        value = "Fail"
    return value
    


#TODO-2: Write your code below to add the grades to student_grades.👇
value=''
for key in student_scores:
    student_grades[key] = convertToGrade(student_scores[key],value)
    print(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)
