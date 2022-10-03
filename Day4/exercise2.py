
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number = len(names) -1
randomint=  random.randint(0,number)
print(f'{names[randomint]} is going to pay the bill')