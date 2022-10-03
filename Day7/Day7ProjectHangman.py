hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#random word genertor
#more about random words https://stackoverflow.com/questions/18834636/random-word-generator-python
from random_word import RandomWords
from regex import F
from sqlalchemy import false, true
r = RandomWords()
# Return a single random word
word = r.get_random_word()
#print(word)






#testing


toPrint =['-']*len(word)


def lifecase(life):
  if life ==1:
    print(hangman[5])
  elif life==2:
    print(hangman[4])
  elif life==3:
    print(hangman[3])
  elif life==4:
    print(hangman[2])
  elif life==5:
    print(hangman[1])
  elif life==6:
    print(hangman[0])

def checkspell(word,alphabet,toprint):
    for i in range(0,len(word)):
        if alphabet ==word[i]:
            toprint[i]=word[i]

            
life=6
print("Welcome to Hangman game! guess the word")
print(hangman[0])
while life>0:
    
    guessWord = input("Write the Alphabet")
    checkspell(word,guessWord,toPrint)
    if guessWord not in word:
      life-=1
    if life ==0:
      print("you have no life left")
      break

    print(f'you have {life} lifes')
    lifecase(life)
    print(''.join(toPrint))
print(hangman[6])