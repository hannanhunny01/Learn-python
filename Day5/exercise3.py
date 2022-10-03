#Write your code below this row 👇
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

sum=0
for i in range(0,101,2):
    
    sum +=i
print(sum)

#0ther way
sum2=0
for i in range(0,101):
    if i%2==0:
        sum2+=i
print(sum2)