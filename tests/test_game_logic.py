import unittest
from game.player import Player
from game.game_logic import Game21

class TestGameLogic(unittest.TestCase):
    """Testklass för spelogiken i Game21-klassen"""
    
    def setUp(self):
        """Setup som körs före varje test"""
        self.game = Game21()
        self.game.player.wins = 0
        self.game.dealer.wins = 0
    
    def test_winner_determination(self):
        """Testar vinnarbestämmelse i olika scenarier"""
        # Test 7: Spelaren vinner när dealern är busted
        self.game.player.score = 18
        self.game.dealer.score = 22
        self.game.dealer.is_busted = True
        
        result = self.game.determine_winner()
        self.assertEqual(result, "player")
        self.assertEqual(self.game.player.wins, 1)
        self.assertEqual(self.game.dealer.wins, 0)
        
        # Test 8: Dealer vinner när spelaren är busted
        self.game.player.score = 23
        self.game.player.is_busted = True
        self.game.dealer.score = 19
        self.game.dealer.is_busted = False
        
        self.game.player.wins = 0
        self.game.dealer.wins = 0
        
        result = self.game.determine_winner()
        self.assertEqual(result, "dealer")
        self.assertEqual(self.game.dealer.wins, 1)
        self.assertEqual(self.game.player.wins, 0)
    
    def test_tie_conditions(self):
        """Testar oavgjorda scenarier"""
        # Test 9: Båda busted - oavgjort
        self.game.player.score = 25
        self.game.player.is_busted = True
        self.game.dealer.score = 24
        self.game.dealer.is_busted = True
        
        result = self.game.determine_winner()
        self.assertEqual(result, "draw")
        self.assertEqual(self.game.player.wins, 0)
        self.assertEqual(self.game.dealer.wins, 0)
        
        # Test 10: Samma poängskillnad - oavgjort
        self.game.player.score = 18
        self.game.dealer.score = 18
        
        result = self.game.determine_winner()
        self.assertEqual(result, "draw")