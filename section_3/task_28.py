player_1 = input('Choose: /rock /paper /scissors ')
player_2 = input('Choose: /rock /paper /scissors ')
if player_1 == player_2:
    print('Result: Equality')
elif (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'paper' and player_2 == 'rock') or (player_1 == 'scissors' and player_2 == 'paper'):
    print('Winner: player_1')
elif (player_2 == 'rock' and player_1 == 'scissors') or (player_2 == 'paper' and player_1 == 'rock') or (player_2 == 'scissors' and player_1 == 'paper'):
    print('Winner: player_2')