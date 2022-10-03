print("welcome to the tip calculator")
bill = float(input('what was the bill? $'))
percent = float(input('percentage of tip you would like ot give? '))
people = int(input('number of people you want to split the bill?'))

bill_with_tip = bill+(bill*(percent/100))
split_in_people = bill_with_tip/people
print("each person should pay: "+str(format(split_in_people,'.2f')))