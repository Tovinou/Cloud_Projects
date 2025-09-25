"""
Tärningsspelet 21 - A Blackjack-like dice game
"""

__version__ = "1.0.0"
__author__ = "Komlan"

from .player import Player
from .game_logic import Game21
from .highscore import HighscoreManager
from .ui import GameUI