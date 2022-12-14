class CheckResult:
    
    def __init__(self, field, player_name, counter):
        self.field = field
        self.player_name = player_name
        self.mark = 'O' if self.player_name == 'A' else 'X'
        self.counter = counter 
     
    def result(self):
        if self.field[1] == self.mark and self.field[2] == self.mark and self.field[3] == self.mark or\
           self.field[4] == self.mark and self.field[5] == self.mark and self.field[6] == self.mark or\
           self.field[7] == self.mark and self.field[8] == self.mark and self.field[9] == self.mark or\
           self.field[1] == self.mark and self.field[4] == self.mark and self.field[7] == self.mark or\
           self.field[2] == self.mark and self.field[5] == self.mark and self.field[8] == self.mark or\
           self.field[3] == self.mark and self.field[6] == self.mark and self.field[9] == self.mark or\
           self.field[1] == self.mark and self.field[5] == self.mark and self.field[9] == self.mark or\
           self.field[3] == self.mark and self.field[5] == self.mark and self.field[7] == self.mark:
            print(f'\n"{self.player_name}" player has won!')
            return 'winner'
        elif self.counter > 7:
            print('\nDraw!')
            return 'draw'