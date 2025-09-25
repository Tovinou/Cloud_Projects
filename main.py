#!/usr/bin/env python3
"""
Huvudentry point för Tärningsspelet 21
"""
from game.game_logic import Game21
from game.ui import GameUI

def main():
    """Huvudfunktion för spelet"""
    game = Game21()
    ui = GameUI()
    
    ui.show_welcome()
    round_number = 1
    
    while True:
        ui.show_round_start(round_number)
        
        result = game.play_round()
        if result is False:  # Spelaren avbröt
            break
        
        ui.show_round_result(game)
        ui.show_winner(result)
        ui.show_scoreboard(game)
        
        if not ui.ask_play_again():
            print("\nTack för spelet!")
            break
        
        round_number += 1

if __name__ == "__main__":
    main()