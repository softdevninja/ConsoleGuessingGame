#!/usr/bin/env python3
# *_* coding: utf-8 *_*
"""
Runs a console game called Hot & Cold

"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

from moderator import Moderator


def main() -> None:
    """
    Main entry point & activates the game moderator.

    Returns:
        None: N/A
    """
    game_moderator = Moderator()
    print(f"Starting game...")

    while game_moderator.get_activity():
        game_moderator.start_game()

    game_moderator.exit_game()


if __name__ == "__main__":
    main()
