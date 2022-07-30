import random
computer_wins = 0
player_wins = 0
i = 0
print('Lets play rock paper scissors')
for i in range(5):
    computer_pick = random.randint(0, 2)
    if computer_pick == 0:
        computer_pick = 'rock'
    if computer_pick == 1:
        computer_pick = 'paper'
    if computer_pick == 2:
        computer_pick = 'scissors'
    player_pick = str(input())
    if player_pick == 'rock' and computer_pick == 'rock':
        print(computer_pick)
        print('DRAW')
        i += 1
    elif player_pick == 'rock' and computer_pick == 'paper':
        print(computer_pick)
        print('The computer wins a point')
        i += 1
        computer_wins += 1
    elif player_pick == 'rock' and computer_pick == 'scissors':
        print(computer_pick)
        print('You win a point')
        i += 1
        player_wins += 1
    elif player_pick == 'paper' and computer_pick == 'paper':
        print(computer_pick)
        print('DRAW')
        i += 1
    elif player_pick == 'paper' and computer_pick == 'rock':
        print(computer_pick)
        print('You win a point')
        i += 1
        player_wins += 1
    elif player_pick == 'paper' and computer_pick == 'scissors':
        print(computer_pick)
        print('The computer wins a point')
        i += 1
        computer_wins += 1
    elif player_pick == 'scissors' and computer_pick == 'paper':
        print(computer_pick)
        print('You win a point')
        i += 1
        player_wins += 1
    elif player_pick == 'scissors' and computer_pick == 'rock':
        print(computer_pick)
        print('The computer wins a point')
        i += 1
        computer_wins += 1
    elif player_pick == 'scissors' and computer_pick == 'scissors':
        print(computer_pick)
        print('Draw')
        i += 1
        player_wins += 1
if player_wins > computer_wins:
    print('YOU WIN')
elif player_wins < computer_wins:
    print('THE COMPUTER WINS')