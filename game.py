from console_clear import ConsoleClear
from check_result import CheckResult
import ascii_art

class Game:
    
    def __init__(self, field):  
        
        self.player_name = 'A'         
        game_is_on = True
        count = 0
        a_score = 0
        b_score = 0
        
        def show_scores():
            print(f'Scores: A player: {a_score}')
            print(f'        B player: {b_score}\n')
        
        def refresh_the_field():
            print(ascii_art.logo)
            show_scores()
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
        
        def change_player():
            if self.player_name == 'A':
                self.player_name = 'B'
            else:
                self.player_name = 'A'
            

        while game_is_on:  

            refresh_the_field()
    
            selected_field = input(f'\n{self.player_name} player --> Select a field: ')
            if len(selected_field) == 1 and selected_field != '0':
                try:
                    field[int(selected_field)]
                except:
                    ConsoleClear()
                    print('Use only valid digit!\n')
                else:
                    if field[int(selected_field)] != 'O' and field[int(selected_field)] != 'X':
                        try:
                            if self.player_name == 'A':
                                field[int(selected_field)] = 'O'    
                            else: 
                                field[int(selected_field)] = 'X'              
                        except:
                            ConsoleClear()
                            print('Use only valid digit!\n')
                        else:
                            ConsoleClear()
                            refresh_the_field()
                            check = CheckResult(field=field, player_name=self.player_name, counter=count)
                            game_over = check.result()
                            
                            if game_over == 'winner' or game_over == 'draw':
                                if game_over == 'winner':
                                    if self.player_name == 'A':
                                        a_score += 1
                                    else:
                                        b_score += 1
                                
                                ConsoleClear()
                                refresh_the_field()
                                check.result()
                                continue_the_game = input("\nDo you want to countinue the game? Type 'yes' or 'no': ").lower()
                                
                                if continue_the_game != 'yes':
                                    game_is_on = False
                                else:
                                    ConsoleClear()
                                    reset_field()
                                    count = 0
                                    change_player()
                            else: 
                                count += 1
                                change_player()
                                ConsoleClear()
                    else:
                        ConsoleClear()
                        print('Field is already used. Choose another field!\n') 
            else:
                ConsoleClear()
                print('Use only valid digit!\n')
        
        ConsoleClear()
        show_scores()
        print(ascii_art.bye)