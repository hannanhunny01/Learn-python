def add_binary(a, b):
  c =a +b
  string = ''
  while c>=1:
    
    if c % 2 == 0:
      string += str('0')

    elif c % 2 != 0 and c!=1:
      
      c-=1
   
      
      string += str('1')
    
    elif c == 1:
    
      
      string += str('1')
      c-=1
    c = c / 2
  return(string[::-1])

def persistence(n):
    # your code
    count = 0
    n= str(n)
    if len(n)==1:
        return 0
    for i in range(0,len(n)):
      if i==0:
        c = int(n[i])
      else:
        c = c* int(n[i])
    count+=1
   
    return count+ persistence(c)
      
      
  
def divisible_count(x,y,k):
        
    count = 0
    if x % k == 0:
        count += 1
    count += int((y / k) - (x / k))
    return count 
     
a = "4of Fo1r pe6ople g3ood th5e the2"
def order(sentence):
    sentence = sentence.split(' ')
    secondList =[]   
    for i in range(0,len(sentence)):
 #       print(sentence[i])
        for j in range(0,len(sentence[i])):
 #         print(sentence[i][j])
          for k in range(1,10):
          #  print(k)
            if sentence[i][j]==str(k):
             
              secondList.insert(k-1,sentence[i])
   
    for i in range(0,len(secondList)):
 #       print(sentence[i])
      
        for j in range(0,len(secondList[i])):
 #         print(sentence[i][j])
          for k in range(1,10):
            secondList = [w.replace(str(k), '') for w in secondList]
              
    
    return " ".join(secondList)
    
  

def order2(sentence):
    if sentence == '':
      return ''
    sentence = sentence.split(' ')
    
    secondList =['-']*len(sentence)
    
    for i in range(0,len(sentence)):
 #       print(sentence[i])
        for j in range(0,len(sentence[i])):
 #         print(sentence[i][j])
          for k in range(0,10):
          #  print(k)
            if sentence[i][j]==str(k):
              secondList[k-1]=sentence[i]
        #      secondList.insert(int(k)-1,sentence[i])
              
          print(secondList)
    return " ".join(secondList)
    
              

a ="O tempora o mores !"
def pig_it(text):
  text = text.split(' ')
  print(text)
  for i in range(0,len(text)):
    if text[i].isalpha() :
      
      first = text[i][0]
      text[i] =text[i][1:]+first+str('ay')
  return ' '.join(text)


arr=["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

def dirReduc(arr):
  NORTH = 0
  SOUTH =0   #bad inteprettaion of instructions have to do again 
  EAST=0
  WEST=0
  direction=[]
  for i in range(0,len(arr)):
    if arr[i] == "NORTH":
      NORTH+=1
    elif arr[i]=="SOUTH":
      SOUTH+=1
    elif arr[i]=="EAST":
      EAST+=1
      
    elif arr[i]=="WEST":
      WEST+=1
      
      
  if NORTH ==SOUTH:
    NORTH=0
    SOUTH=0
  if EAST==WEST:
    EAST=0
    WEST=0
  if EAST>WEST:
    EAST=EAST-WEST
    WEST=0
  if WEST>EAST:
    WEST=WEST-EAST
    EAST=0
  if NORTH>SOUTH:
    NORTH=NORTH-SOUTH
    SOUTH=0
  else:
    SOUTH =SOUTH-NORTH
    NORTH=0
  if NORTH!=0:
    north =["NORTH"]*NORTH
    
    direction.extend(north)
  if SOUTH!=0:
    south =["SOUTH"]*SOUTH
    direction.extend(south)
  if WEST!=0:
    west =["WEST"]*WEST
    direction.extend(west)
  if EAST!=0:
    east=["EAST"]*EAST
    direction.extend(east)
  return direction


def dirReduc(arr):
  direction=[]
  for i in range(0,len(arr)):
    
    if arr[i]=="NORTH"and arr[i+1]=="SOUTH":
      arr[i] = "NULL"
      arr[i+1]="NULL"
    elif arr[i]=="EAST"and arr[i+1]=="WEST":
      arr[i] = "NULL"
      arr[i+1]="NULL"
    
     
    elif arr[i]!="NULL":
      print(direction)
      direction.append(arr[i])
      
  return direction


opposites = { "NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST" }

def dirReduc(arr): 
    new_list = [] 
    for i in range(0,len(arr)): 
        if len(new_list) == 0: 
            new_list.append(arr[i]) 
        elif new_list[-1] != opposites[arr[i]]: 
            new_list.append(arr[i]) 
        else: 
            new_list.pop() 
    return new_list


string ="100 180 90 56 65 74 68 86 99"
this_dict={}
def returnSoma(string):
  soma=0
  for i in range(0,len(string)):
    soma = soma+ int(string[i])
  return soma
def order_weight(string):
  strng = string.split(' ')
  for i in range(0,len(string)):
    this_dict[strng[i]]= returnSoma(string[i])
  print(this_dict)

#order_weight(string)

def fizzbuzz(n):
    vetor=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            vetor.append("FizzBuzz") 
        elif i%3==0:
            vetor.append("Fizz")
        elif i%5==0:
            vetor.append("Buzz")
        else:
            vetor.append(a)
    return vetor

intervals =[
   [0, 20],
   [-100000000, 10],
   [30, 40]
]
def last_digit(n1, n2):
    b =n1**n2
    c= str(b)
    
    
    return c[-1]
print(last_digit(4, 1))
  
def likes(names):
    # your code here
    
        if len(names) == 0:
            return  "no one likes this"
        if len(names) == 1:
            return names[0]+" likes this"
        if len(names) ==2:
            return names[0]+" and "+names[1]+" like this"
        
        if len(names) ==3:
            return names[0]+", "+names[1] + " and " + names[2]+" like this"
    
        if len(names)>3:
            y = len(names)-2
            return names[0]+", "+names[1] +" and "+ str(y)+" others like this"


def create_phone_number(n):
    y=""
    count =0
    for x in n:
        if count ==0:
            y = y+"("
        if count ==3:
            y= y+")"
            y=y+" "
        if count ==6:
            y=y+"-"
            
            
        y = y + str(x)
        count = count +1
    
    return y

