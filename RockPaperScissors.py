import random

def play():
    user = input(" Choose one: Rock 'r', Paper 'p', Scissors 's' \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    print(computer)
    if winner(user, computer):
        return 'You win!'
    
    return 'You lost!'

def winner(player, opp): #opp for 'opponent'

    if player or opp == 's' and player or opp == 'p' \
    and player or opp == 'p' and player or opp == 'r':
        return True

print(play())