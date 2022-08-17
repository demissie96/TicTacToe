from console_clear import ConsoleClear

def playing_the_game(player_name):    
    global player
    
    selected_field = input(f'\n{player_name} player --> Select a field: ')
    if len(selected_field) == 1:
        if field[int(selected_field)] != 'O' and field[int(selected_field)] != 'X':
        
            try:
                if player_name == 'A':
                    field[int(selected_field)] = 'O'    
                else: 
                    field[int(selected_field)] = 'X'              
            except:
                ConsoleClear()
                print('Use only valid digit!\n')
            else:
                
                if player_name == 'A':
                    player = 'B'
                else:
                    player = 'A'
                ConsoleClear()
        else:
            ConsoleClear()
            print('Field is already used. Choose another field!\n') 
    else:
        ConsoleClear()
        print('Use only valid digit!\n')

ConsoleClear()

field = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

game_is_on = True
player = 'A'

while game_is_on:

    print(f' {field[1]} | {field[2]} | {field[3]} ')
    print('-----------')
    print(f' {field[4]} | {field[5]} | {field[6]} ')
    print('-----------')
    print(f' {field[7]} | {field[8]} | {field[9]} ')
    
    if player == 'A':
        playing_the_game(player)
    else:
        playing_the_game(player)