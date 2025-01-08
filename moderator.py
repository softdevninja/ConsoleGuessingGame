import sys
from dataclasses import dataclass

# TODO:
#   - While game is acive player has choice to continue
#   - Track number of guesses
#   - Define range 1 - 100
#   - Use hot & cold until the number is guessed

@dataclass
class Moderator:
    __slots__ = ('guesses', 'magic', 'is_active')
    
    def __init__(self) -> None:
        self.guesses : int = None
        self.magic : int = None 
        self.is_active : bool = True
    
    def exit_game(self) -> None:
        sys.exit(0)
    
    def start_game(self) -> None:
        user_selection = input(f'\n Please select a number between 1 - 100: ')
        
    def set_activity(self, continue_game : bool) -> None:
        self.is_active = continue_game
        
    def get_activity(self) -> bool:
        return self.is_active
        
