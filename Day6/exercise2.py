
#Prime numbers are numbers that can only be cleanly divided by themselves and 1.




#Write your code below this line 👇


def prime_checker(n):
    if(n==1 or n==2 or n==3):
        print("Prime Number")
        return
    for i in range(2,n):
        if n%i==0:
            print("It\'s not a prime number.")
            return
    print("It\'s a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(n)
