player_one = input('Enter rock, paper, or scissors ')
player_two = input('Enter rock, paper, or scissors ')

if player_one == player_two:
    print('its a tie')
elif player_one == 'rock' and player_two != 'paper':
    print('player one wins')
elif player_one == 'paper' and player_two != 'scissors':
    print('player one wins')

elif player_one == 'scissor' and player_two != 'rock':
    print('player one wins')
else:
    print('player two wins')
