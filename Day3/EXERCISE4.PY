#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.




# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepForSmall =2
pepForLarge = 3
extracheese = 1
totalprize=0

if size == "S":
    totalprize +=small_pizza
    if add_pepperoni =="Y":
        totalprize+=pepForSmall
    if extra_cheese=='Y':
        totalprize+=extracheese
elif size =="M":
    totalprize +=medium_pizza
    if add_pepperoni =="Y":
        totalprize+=pepForLarge
    if extra_cheese=='Y':
        totalprize+=extracheese

else:
    totalprize+= large_pizza
    if add_pepperoni =="Y":
        totalprize+=pepForLarge
    if extra_cheese=='Y':
        totalprize+=extracheese

print("your final price is :$"+str(totalprize)+".")
    