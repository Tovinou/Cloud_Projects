import unittest
from game.player import Player
from game.game_logic import Game21

class TestIntegration(unittest.TestCase):
    """Integrationstester för hela spelflödet"""
    
    def setUp(self):
        self.game = Game21()
    
    def test_complete_round_flow(self):
        """Testar ett komplett spelrundeflöde"""
        # Simulera en grundläggande runda
        self.game.player.reset_round()
        self.game.dealer.reset_round()
        
        # Spelaren slår tärningen
        roll = self.game.player.roll_dice()
        self.assertIn(roll, range(1, 7))
        
        # Kontrollera att poängen uppdateras
        self.assertEqual(self.game.player.score, roll)