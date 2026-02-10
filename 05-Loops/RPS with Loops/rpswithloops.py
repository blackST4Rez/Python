import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain:
    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerChoice = input('\nEnter...\n1. Rock,\n2. Paper,\n3. Scissors\n\n')

    # Casting user input from string to an integer
    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit('You must enter 1, 2, or 3.')
        
    computerChoice = random.choice('123')
        
    # Casting computer generated string into an integer
    computer = int(computerChoice)
        
    print('\nYou chose ' + str(RPS(player)).replace('RPS.','') + '.')
    print(' Computer ' + str(RPS(computer)).replace('RPS.','') + '.\n')

    if player == 1 and computer == 3:
        print('You Win!')
    elif player == 2 and computer ==1:
        print('You Win!')
    elif player == 3 and computer == 1:
        print('You Win!')
    elif player == computer:
        print('Tie!')
    else:
        print('Computer Won!\n')

    playagain = input('\nPlay Again ? \nY for YES or\nN for NO \n\n')
    
    if playagain.lower() == 'y':
        continue
    else:
        print('\nHave a good day!')
        print('Thank you for playing!\n')
        playagain = False
        
        sys.exit('Made with 💜 by Raka.')
        