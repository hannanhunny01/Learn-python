from logo import logo,vs
from data import data
import random
SCORE =0
numberofA=0
numberofB=0
FOLLOWER=0
num = random.randint(0,len(data)-1)
def start(compareA,compareB):
    print(logo)
    if SCORE>0:
        print(f"You are Right! Current Score{SCORE}")
    print(f"Compare A: {compareA}")
    print(vs)
    print(f"Compare B: {compareB}")

def checkanswer():
    answer =input('who Has more followers? \'A\' or \'B\'')
    return answer

def returnPeople(n):
    name = data[n]['name']
    follower = data[n]['follower_count']
    desc= data[n]['description']
    country = data[n]['country']

    return str(name)+" ,"+str(desc)+" ,"+str(country)


def checkFollower(numbA,numbB):
    followerA = data[numbA]['follower_count']
    followerB = data[numbB]['follower_count']

    if followerA>followerB:
        return "A"
    else:
        return "B"

def makeNumber():
    return random.randint(0,len(data)-1)    

PLAY_AGAIN ="yes"

while PLAY_AGAIN=='yes':
    numberofB=makeNumber()
    if numberofA==numberofB:
        while numberofA==numberofB:
            numberofB=makeNumber()
    personA=returnPeople(numberofA)
    personB=returnPeople(numberofB)

    start(personA,personB)
    followers = checkFollower(numberofA,numberofB)

    answer =checkanswer()
    if answer ==followers:
        SCORE+=1
        numberofA= numberofB
    else:
        print("You are Wrong")
        SCORE=0
        PLAY_AGAIN = input('Want to play again? yes or no')
        if PLAY_AGAIN =="yes":
            NEW_GAME='yes'