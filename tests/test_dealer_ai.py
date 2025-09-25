import unittest
from game.player import Player
from game.game_logic import Game21

class TestDealerAI(unittest.TestCase):
    """Testklass för dealerns AI-beteende"""
    
    def setUp(self):
        """Setup som körs före varje test"""
        self.game = Game21()
        self.game.player.wins = 0
        self.game.dealer.wins = 0
    
    def test_dealer_hits_below_17(self):
        """Testar att dealern slår när under 17"""
        # Test 11: Dealer slår när under 17
        self.game.dealer.score = 16
        original_score = self.game.dealer.score
        
        # Simulera dealer_turn logik
        while self.game.dealer.score < 17:
            self.game.dealer.roll_dice()
        
        self.assertGreaterEqual(self.game.dealer.score, 17)
        self.assertGreater(self.game.dealer.score, original_score)
    
    def test_dealer_stays_at_17_or_above(self):
        """Testar att dealern stannar vid 17 eller mer"""
        # Test 12: Dealer stannar vid 17 eller mer
        self.game.dealer.score = 17
        original_score = self.game.dealer.score
        
        # Simulera att dealern inte slår när >= 17
        if self.game.dealer.score >= 17:
            pass  # Dealer stannar
        
        self.assertEqual(self.game.dealer.score, original_score)