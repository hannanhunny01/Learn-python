rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#0=rock ,1=paper ,2 = scissors
import random
print("Welcome to rock paper scissors game")
user_choice = input("please choose \"Rock\",\"Paper\" or \"Scissors\"")
if user_choice =="Rock":
    print(f'you have choosed\n,{rock}')
elif user_choice =="Paper":
    print(f'you have choosed\n,{paper}')
elif user_choice =="Scissors":
    print(f'you have choosed\n,{scissors}')
computer_choice = random.randint(0,2)

def selection(n):
    if n == 0:
        print(f"Computer has Choosed\n{rock}")
    if n==1:
        print(f"Computer has Choosed\n{paper}")
    if n==2:
        print(f"Computer has Choosed\n{scissors}")
selection(computer_choice)
if user_choice==computer_choice:
    print("Its a tie")
elif user_choice=="Rock" and computer_choice==1:
    print("Computer Won")
elif user_choice=="Rock" and computer_choice==2:
    print("You Won")
elif user_choice=="Paper" and computer_choice==0:
    print("You Won")
elif user_choice=="Paper" and computer_choice==2:
    print("Computer Won")
elif user_choice=="Scissors" and computer_choice==0:
    print("Computer Won")
elif user_choice=="Scissors" and computer_choice==1:
    print("You Won")