logo =''' _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ '''

import random
print(logo)
life=0
print('Guess number between 1 to 100')
difficulty =input('Chose dificult type \'easy\' or \'hard\'\n')
if difficulty == 'easy':
    life =10
else:
    life=5

number = random.randint(1,100)
while life>0:
    guess = int(input('Make a guess  '))
    if guess == number:
        print('Congratulation you guessed it')
        break
    elif guess>number:
        print('too High') 
        life-=1
        print(f'you have {life} left')
    elif guess<number:
        print('too Low')
        life-=1
        print(f'you have {life} left')
if life==0:
    print('you lost')
    print(f'the number was {number}' )
    