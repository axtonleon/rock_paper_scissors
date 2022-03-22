import random
total_amount_of_moves = int(input('how many are we going: '))
moves_list = {'scissors':1,'rock':2 ,'paper':3}
moves = [1, 2, 3]
print('here we go again')
move_count = 1
win = 0
lose = 0
while move_count <= total_amount_of_moves:
    n = input('whats your move: ')
    move_count += 1
    if n in moves_list:
        computer_play = random.choice(list(moves_list))
        print(computer_play)
        if n == ('rock') and computer_play == ('scissors'):
            win += 1
            print('you win my man')
        elif n  == ('paper') and computer_play == ('rock'):
            win += 1
            print('Abeg calm down boss')
        elif n  == ('scissors') and computer_play == ('paper'):
            win += 1
            print('comrade small small na')
        elif n  == computer_play:
            print('No dey drag with me')
        else:
            lose += 1 
            print('ha ha ha you no good')

    else:
        print('comrade no be so')
else:
    print("bruh, that's the end")
if win > lose:
    print('big man win me sha')
else:
    print('''you lose
shey you fit good like this''')
    
    
        
    
    
