#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


years_left= 90-age
days_left = years_left*365
weeks_left = days_left/7
int(weeks_left)
months_left = days_left/30
print("you have "+str(days_left)+" days,"+str(weeks_left)+" weeks ,"+str(int(months_left))+" months left.")


