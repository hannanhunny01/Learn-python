
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


# 🚨 Don't change the code below 👇

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi= weight/(height*height)
print(str(weight)+" / ("+str(height)+" x "+str(height)+") = "+ str(bmi))
print(int(bmi))