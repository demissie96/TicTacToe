import os

class ConsoleClear:

    def __init__(self):
        os.system('cls' if os.name=='nt' else 'clear')
    
    