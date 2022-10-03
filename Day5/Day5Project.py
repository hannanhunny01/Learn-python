import random

from numpy import number
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

letters_chosed = []
number_chosed =[]
symbols_chosed =[]

for i in range(0,nr_letters):
    choose_letter = random.randint(0,len(letters)-1)
    letters_chosed.append(letters[choose_letter])
for i in range(0,nr_symbols):
    chose_symbol= random.randint(0,len(symbols)-1)
    symbols_chosed.append(symbols[chose_symbol])
for i in range(0,nr_numbers):
    chose_number = random.randint(0,len(numbers)-1)
    symbols_chosed.append(numbers[chose_number])

final_list = letters_chosed+number_chosed+symbols_chosed

print(final_list)
random.shuffle(final_list)
print(''.join(final_list))


