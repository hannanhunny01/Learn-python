#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bmi = weight / height x height
bmi = weight/(height*height)

if bmi < 18.5:
    print("you are are underweight")
elif bmi >18.5 and bmi<25:
    print("you have a normal weight")
elif bmi>25 and bmi<30:
    print("you are slightly overweight")
elif bmi >30 and bmi<35:
    print("you are overwieght")
else:
    print("you are clinically ovewight")

