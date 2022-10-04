logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


encryptedMessage =[]
decryptedMessage =[]

def convertString(string):
    list=[]
    list[:0]=string
    return list


def ceasercipherEncrypt(text,shift):
    a = convertString(text)
    for i in range(0,len(a)):
        for j in range(0,len(alphabet)):
            if a[i]==alphabet[j]:
                if j+shift>25:
                    number = ((j+shift)%25)-1
                    encryptedMessage.append(alphabet[number])
                else:
                    encryptedMessage.append(alphabet[j+shift])


def ceasercipherDecrypt(text,shift):
    a = convertString(text)
    for i in range(0,len(a)):
        for j in range(0,len(alphabet)):
            if a[i]== alphabet[j]:
               decryptedMessage.append(alphabet[j-shift])
again = "yes"
while again== 'yes':
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=='encode':
        ceasercipherEncrypt(text,shift)
        print("".join(encryptedMessage))
    else:
        ceasercipherDecrypt(text,shift)
        print("".join(decryptedMessage))
    
    again = input("Want to Encrypt or Decrypt Again? \'yes\' or \'no\'")
