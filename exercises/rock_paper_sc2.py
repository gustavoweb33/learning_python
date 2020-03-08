import random

player_one = input('Enter rock, paper, or scissors ').lower()
computer = random.randint(0, 2)
computer_choise = None

if computer == 0:
    computer_choise = 'rock'
elif computer == 1:
    computer_choise = 'paper'
else:
    computer_choise = 'scissors'

print(f'Computer plays {computer_choise}')

if player_one == computer_choise:
    print('its a tie')
elif player_one == 'rock' and computer_choise != 'paper':
    print('player one wins')
elif player_one == 'paper' and computer_choise != 'scissors':
    print('player one wins')

elif player_one == 'scissor' and computer_choise != 'rock':
    print('player one wins')
else:
    print('player two wins')
