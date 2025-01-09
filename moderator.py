import sys
import random
from dataclasses import dataclass

# TODO:
#   - Add documentation


@dataclass
class Moderator:
    __slots__ = ("guesses", "magic", "is_active")

    def __init__(self) -> None:
        self.guesses: int = 0
        self.magic: int = None
        self.is_active: bool = True

        self.magic = random.randint(1, 100)

    def exit_game(self) -> None:
        sys.exit(0)

    def start_game(self) -> None:
        user_selection: int = int(input(f"Please select a number between 1 - 100: "))
        self.guesses += 1

        if user_selection == self.magic:
            print(f"You have won the game with #{self.guesses} of tries.")
            self.is_active = False
        else:
            threshold: int = 10
            diff: int = user_selection - self.magic

            if diff < 0:
                diff = diff * -1

            if diff > 10:
                print(f"You are getting cold!")
            else:
                print(f"You are getting warm!")

    def set_activity(self, continue_game: bool) -> None:
        self.is_active = continue_game

    def get_activity(self) -> bool:
        return self.is_active
