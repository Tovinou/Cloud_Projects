"""
Huvudstartfil för Blackjack-spelet.
"""
from .game import Game

def main():
    """Startar spelet"""
    game = Game()
    game.run()

if __name__ == "__main__":
    main()