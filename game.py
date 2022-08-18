from console_clear import ConsoleClear
from check_result import CheckResult
import ascii_art

class Game:
    
    def __init__(self, field):  
        
        player_name = 'A'         
        game_is_on = True
        count = 0
        
        def refresh_the_field():
            print(ascii_art.logo)
            print(f' {field[1]} | {field[2]} | {field[3]} ')
            print('-----------')
            print(f' {field[4]} | {field[5]} | {field[6]} ')
            print('-----------')
            print(f' {field[7]} | {field[8]} | {field[9]} ')  
        
        def reset_field():
            field[1] = '1'
            field[2] = '2'
            field[3] = '3'
            field[4] = '4'
            field[5] = '5'
            field[6] = '6'
            field[7] = '7'
            field[8] = '8'
            field[9] = '9'

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
                            continue_the_game = input("\nDo you want to countinue the game? Type 'yes' or 'no': ").lower()
                            if continue_the_game != 'yes':
                                game_is_on = False
                            else:
                                ConsoleClear()
                                reset_field()
                                count = 0
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
        
        ConsoleClear()
        print(ascii_art.bye)