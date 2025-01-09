import sys
import random
from dataclasses import dataclass


@dataclass
class Moderator:
    """
    A class to represent a game moderator
    """

    __slots__ = ("guesses", "magic", "is_active")

    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the moderator object.

        Returns:
        """
        self.guesses: int = 0
        self.magic: int = None
        self.is_active: bool = True

        self.magic = random.randint(1, 100)

    def exit_game(self) -> None:
        """
        Exits the game, when called.

        Returns:
            None: N/A
        """
        sys.exit(0)

    def start_game(self) -> None:
        """
        Start the game by sequence.
        - Ask user for a selection
        - Determine if selection is on point
        - If not, guide user to make a better selection by hinting warms & cold levels

        Returns:
            None: N/A
        """
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
        """
        Extended fundtionality to set the game status from outside of the moderator object

        Args:
            continue_game (bool): Will assign the status to class member which check to see if the game is active

        Returns:
            None: N/A
        """
        self.is_active = continue_game

    def get_activity(self) -> bool:
        """
        Return game activity status.

        Returns:
            bool: returns the current activity status of the game.
        """
        return self.is_active
