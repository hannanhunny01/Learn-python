# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(student_heights)

total_height =0
count =0
for x in range(0,len(student_heights)):
    total_height +=student_heights[x]
    count+=1
avg_height = total_height/count
print(round(avg_height))