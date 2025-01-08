#!/usr/bin/env python3
# *_* coding: utf-8 *_*
from moderator import Moderator

def main() -> None: 
    game_moderator = Moderator()
    print(f'Starting game...')
    
    while (game_moderator.get_activity()):
        game_moderator.start_game()

if __name__ == "__main__":
    main()