from console_clear import ConsoleClear

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
player = 'a'

while game_is_on:

    print(f' {field[1]} | {field[2]} | {field[3]} ')
    print('-----------')
    print(f' {field[4]} | {field[5]} | {field[6]} ')
    print('-----------')
    print(f' {field[7]} | {field[8]} | {field[9]} ')
    
    if player == 'a':
        selected_field_a = input('\nA player --> Select a field: ')
        if len(selected_field_a) == 1:
            if field[int(selected_field_a)] != 'O' and field[int(selected_field_a)] != 'X':
            
                try:
                    field[int(selected_field_a)] = 'O'
                    player = 'b'
                    ConsoleClear()
                except:
                    ConsoleClear()
                    print('Use only valid digit!\n')
            else:
                ConsoleClear()
                print('Field is already used. Choose another field!\n') 
        else:
            ConsoleClear()
            print('Use only valid digit!\n')
    else:
        selected_field_b = input('\nB player --> Select a field: ')
        if len(selected_field_b) == 1:
            if field[int(selected_field_b)] != 'O' and field[int(selected_field_b)] != 'X':
                
                try:
                    field[int(selected_field_b)] = 'X'
                    player = 'a'
                    ConsoleClear()
                except:
                        ConsoleClear()
                        print('Use only valid digit!\n')
            else:
                ConsoleClear()
                print('Field is already used. Choose another field!\n') 
        else:
            ConsoleClear()
            print('Use only valid digit!\n')
    

    