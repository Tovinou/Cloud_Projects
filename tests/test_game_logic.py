import unittest
from unittest.mock import patch
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

    @patch('random.randint')
    def test_dealer_turn_stops_at_17(self, mock_randint):
        """Testar att dealerns tur stannar vid 17 eller mer."""
        mock_randint.side_effect = [6, 6, 5]
        self.game.dealer_turn()
        self.assertEqual(self.game.dealer.score, 17)
        self.assertFalse(self.game.dealer.is_busted)

    @patch('random.randint')
    def test_dealer_turn_busts_over_21(self, mock_randint):
        """Testar att dealern blir tjock över 21."""
        mock_randint.side_effect = [6, 6, 10]
        self.game.dealer_turn()
        self.assertEqual(self.game.dealer.score, 22)
        self.assertTrue(self.game.dealer.is_busted)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['r', 's'])
    def test_player_turn_roll_and_stand(self, mock_input, mock_randint):
        """Testar att spelaren kan rulla och sedan stanna."""
        self.game.player_turn()
        self.assertEqual(self.game.player.score, 5)
        self.assertEqual(mock_input.call_count, 2)

    @patch('random.randint', return_value=11)
    @patch('builtins.input', side_effect=['r', 'r'])
    def test_player_turn_busts(self, mock_input, mock_randint):
        """Testar att spelaren blir tjock över 21."""
        self.game.player_turn()
        self.assertTrue(self.game.player.is_busted)
        self.assertEqual(self.game.player.score, 22)

    @patch('random.randint', side_effect=[10, 11])
    @patch('builtins.input', side_effect=['r', 'r'])
    def test_player_turn_gets_21(self, mock_input, mock_randint):
        """Testar att spelarens tur avslutas vid 21."""
        self.game.player_turn()
        self.assertEqual(self.game.player.score, 21)
        self.assertFalse(self.game.player.is_busted)

    @patch('builtins.input', side_effect=['x', 'r', 's'])
    @patch('random.randint', return_value=5)
    def test_player_turn_invalid_input(self, mock_randint, mock_input):
        """Testar att ogiltigt val hanteras korrekt."""
        self.game.player_turn()
        self.assertEqual(self.game.player.score, 5)
        self.assertEqual(mock_input.call_count, 3)

if __name__ == '__main__':
    unittest.main()