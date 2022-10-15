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

def last_digit_old(n1, n2):
  b = n1**n2
  c = str(b)

  return c[-1]







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

again = "no"
while again=="yes":
    print("logo")
    action = input("which action you want to do \n1-Divide \n2-Multiply \n3-Addition \n4-Subtraction \n5-module\n")
    a,b = input("Write 1st and 2nd Number with space in between Ex:2 5").split()
    nvalue=0
    again = input("Do You Want to do calculation again \'yes\' or \'no\'")
    if action ==1:
       print(nvalue=div(a,b))
    elif action==2:
       print(nvalue = multiply(a,b))
    elif action==3:
       print(nvalue = add(a,b))

    elif action==4:
      print( nvalue= sub(a,b))
    elif action ==5:
       print(nvalue=module(a,b))


string ="How can mirrors be real if our eyes aren't real"
def to_jaden_case(string):
  string = string.split()
  string3 =[]
  for i in range(0,len(string)):
    string2=list(string[i].strip())
    string2[0]=string2[0].upper()
    for i in range(1,len(string2)):
        string2[i]=string2[i].lower()
    #print(string2)
    
    
    
   # string2[i]=string2[i].upper()
    string3.append("".join(string2))
  return " ".join(string3)
  

text='The sunset sets at twelve o clock.'

def alphabet_position(text):
    postion =["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    value=[]
  
    text = list(text.strip())
    for i in range(0,len(text)):
      for j in range(0,len(postion)):
        if text[i].lower()==postion[j]:
          value.append(j+1)
    value = ' '.join(str(item) for item in value)
    return value

  
unique = ['A', 'B', 'C', 'D', 'A', 'B']
def unique_in_order(unique):
  for i in range(0,len(unique)):
    if i == len(unique)-1:
      continue 
    if unique[i] == unique[i+1]:
      unique.pop(unique[i])
  return unique

numbers ="1 2 3 4 5"
def high_and_low(numbers):
  numbers  = numbers.split(' ')
  numbers = [int(x) for x in numbers]
  high=numbers[0]
  low =numbers[0]
  for i in range(0,len(numbers)):

    if numbers[i]>high:
      high = numbers[i]
    if numbers[i]<low:
      low = numbers[i]
    
    
  return str(high)+" "+str(low)

  
message="EBG13 rknzcyr."
def rot13(message):
    normal="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    normal= list(normal)
    shifted="NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    shifted= list(shifted)
    rot13=[]
    for i in range(0,len(message)):
      if message[i]==" ":
          rot13.append('')
      if message[i].isalpha()!= True:
          rot13.append(message[i])
          continue 
    
      for j in range(0,len(normal)):
       
        
        if message[i]==normal[j]:
          rot13.append(shifted[j])
    return "".join(rot13)
    


arr =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
def max_sequence(arr):
  total=0
  highest=[]
  highest2=[] #highest of each shift 
  if len(arr)==0:
    return 0
  for i in range(0,len(arr)):
    total=0
    j=i
    for j in range(i,len(arr)):
      total += arr[j]
      highest2.append(total)
    highest.append(max(highest2))
    highest2=[]
  if max(highest) ==-1:
    return 0
  return max(highest)

      
      
      

args= [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
def solution(args):
  new_list=[]
  j=0
  i=0
  verify = True

  while i<len(args)-2:
    
    if args[i]+1==args[i+1] and args[i+1]+1==args[i+2]:
      j=i+2
      verify=True
      while verify==True:

        if j+1==len(args):
          verify=False
          continue
       
        if args[j]+1==args[j+1]:
      #    print(args[j]+1==args[j+1])
      #    print(f'{args[j]},,,,,{args[j]+1}')
          j+=1
        else:
         
            
          verify = False
      string = str(args[i])+"-"+str(args[j])
      new_list.append(string)
      i =j+1
    else:
      new_list.append(args[i])
      if i+2==len(args)-1:
            new_list.append(args[i+1])
      if i+1== len(args)-2:
            new_list.append(args[i+2])
      
      i+=1
  new_list = [str(x)for x in new_list]
  return ','.join(new_list)


array =[1,2,3,4,5,6,7]

def josephus2(array,k):
  position =0
  list=[]
  for i in range(0,len(array)):
#    print(i,k)
    if str(array[i])==str(k):
  #    print("hello")
      position = i
      list.append(array[i])         #algo ta errado  :((()))
    #  array.pop(array[position])
    #  print(array)
      break
    
  while len(array)>0:
   if len(array)==1:
      list.append(array[0])
      
      array.pop(array[0])
      return ' '.join([str(x)for x in list])
   position= ((len(array)+position+1)%len(array))-1
   print(position)
   list.append(array[position])
   
  # array.pop(array[position])
   print(list)
  return ' '.join([str(x)for x in list])

  
password="PassW0rd"
def alphanumeric(password):
  array=[]
  for i in range(0,10):
    array.append(str(ord((str(i)))))
  for i in range(0,26):
    array.append(str(ord('a')+i))
  for i in range(0,26):
    array.append(str(ord('A')+i))
  password = list(password)
  password = [str(ord(x)) for x in password]
  if len(password)==0:
    return False

  for i in range(0,len(password)):
    if password[i] not in array:
      return False
   
  return True

sort =[9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
def move_zeros(sort):
  count=0
  i=0
  while i<len(sort):
    if sort[i]==0:
       sort.remove(sort[i])
       count+=1
    else:
      i+=1
  for i in range(0,count):
     sort.append(0)
      
        
  return sort   


def last_digit(a, b):  
    if a == 0 and b == 0:
        return 1
       

    if b == 0:
        return 1
       
    
    if a == 0:
        return 0
    if b % 4 == 0:
        res = 4
    else:
        res = b % 4        
    num = pow(a, res)
    return num % 10
  