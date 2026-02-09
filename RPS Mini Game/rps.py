import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print('')

playerChoice = input('Enter...\n1. Rock,\n2. Paper,\n3. Scissors\n\n')

# Casting user input from string to an integer
player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit('You must enter 1, 2, or 3.')
    
computerChoice = random.choice('123')
    
# Casting computer generated string into an integer
computer = int(computerChoice)
    
print('')
print(' You chose ' + str(RPS(player)).replace('RPS.','') + '.')
print(' Computer ' + str(RPS(computer)).replace('RPS.','') + '.')
print('')

if player == 1 and computer == 3:
    print('You Win!')
elif player == 2 and computer ==1:
    print('You Win!')
elif player == 3 and computer == 1:
    print('You Win!')
elif player == computer:
    print('Tie!')
else:
    print('Computer Won!')
    print('')
    