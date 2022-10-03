#You are going to write a program that tests the compatibility between two people.



# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_name = name1+name2
t = total_name.count('t')
r = total_name.count('r')
u =total_name.count('u')
e = total_name.count('e')
l =total_name.count('l')
o= total_name.count('o')
v=total_name.count('v')
ee=total_name.count('e')

first= t+r+u+e
second = l+o+v+ee

total = str(first)+str(second)
total = int(total)

if total<10 or total>90:
    print("\"Your score is "+str(total)+", you go together like coke and mentos.\"")
elif total>=40 and total<=50:
    print("Your score is "+ str(total) + " , you are alright together.")
else:
    print("you score is "+str(total))

