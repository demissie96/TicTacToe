from console_clear import ConsoleClear
from check_result import CheckResult

class Game:
    
    def __init__(self, field):  
        
        player_name = 'A'         
        game_is_on = True
        count = 0
        
        def refresh_the_field():
            print(f' {field[1]} | {field[2]} | {field[3]} ')
            print('-----------')
            print(f' {field[4]} | {field[5]} | {field[6]} ')
            print('-----------')
            print(f' {field[7]} | {field[8]} | {field[9]} ')        

        while game_is_on:     
            
            refresh_the_field()
    
            selected_field = input(f'\n{player_name} player --> Select a field: ')
            if len(selected_field) == 1 and selected_field != '0':
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
                        ConsoleClear()
                        refresh_the_field()
                        check = CheckResult(field=field, player_name=player_name, counter=count)
                        game_over = check.result()
                        
                        if game_over:
                            print('Game Over')
                            game_is_on = False
                        else: 
                            count += 1
                            
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
        
        print("Hahaha")