from console_clear import ConsoleClear

class Game:
    
    def __init__(self, field):  
        
        player_name = 'A'         
        game_is_on = True

        while game_is_on:

            print(f' {field[1]} | {field[2]} | {field[3]} ')
            print('-----------')
            print(f' {field[4]} | {field[5]} | {field[6]} ')
            print('-----------')
            print(f' {field[7]} | {field[8]} | {field[9]} ')      
    
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
                            player_name = 'B'
                        else:
                            player_name = 'A'
                        ConsoleClear()
                else:
                    ConsoleClear()
                    print('Field is already used. Choose another field!\n') 
            else:
                ConsoleClear()
                print('Use only valid digit!\n')