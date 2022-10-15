from logo import *




def module(a,b):
    return a%b
def multiply(a,b):
    return a*b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b

again = "yes"
while again=="yes":
    print(logo)
    action = int(input("which action you want to do \n1-Divide \n2-Multiply \n3-Addition \n4-Subtraction \n5-module\n"))
    a,b = input("Write 1st and 2nd Number with space in between Ex:2 5\n").split()
    a = int(a)
    b= int(b)
    nvalue=0
   
    if action ==1:
       print(div(a,b))
    elif action==2:
       print(multiply(a,b))
    elif action==3:
       print(add(a,b))

    elif action==4:
      print(sub(a,b))
    elif action ==5:
       print(module(a,b))
    again = input("Do You Want to do calculation again \'yes\' or \'no\'\n")