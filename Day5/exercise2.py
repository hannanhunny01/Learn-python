#You are going to write a program that calculates the highest score from a List of scores.

#input example = 78 65 89 86 55 91 64 89


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score=0
for n in range(0,len(student_scores)):
    current = student_scores[n]
    if current>max_score:
        max_score=current
print(max_score)



