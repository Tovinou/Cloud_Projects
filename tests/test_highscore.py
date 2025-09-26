import unittest
from unittest.mock import patch, mock_open
from game.highscore import HighscoreManager
import json

class TestHighscoreManager(unittest.TestCase):
    """Testklass för HighscoreManager"""

    def setUp(self):
        """Setup som körs före varje test"""
        self.highscore_manager = HighscoreManager(filename="test_highscore.json")

    def test_load_highscore_no_file(self):
        """Testar att ladda highscore när filen inte finns."""
        with patch('os.path.exists', return_value=False):
            result = self.highscore_manager.load_highscore()
            self.assertFalse(result)
            self.assertEqual(self.highscore_manager.player_wins, 0)
            self.assertEqual(self.highscore_manager.dealer_wins, 0)

    def test_load_highscore_file_exists(self):
        """Testar att ladda highscore från en befintlig fil."""
        mock_data = json.dumps({'player_wins': 10, 'dealer_wins': 5})
        with patch('os.path.exists', return_value=True):
            with patch('builtins.open', mock_open(read_data=mock_data)) as mock_file:
                result = self.highscore_manager.load_highscore()
                self.assertTrue(result)
                self.assertEqual(self.highscore_manager.player_wins, 10)
                self.assertEqual(self.highscore_manager.dealer_wins, 5)

    def test_save_highscore(self):
        """Testar att spara highscore."""
        self.highscore_manager.player_wins = 15
        self.highscore_manager.dealer_wins = 8
        with patch('builtins.open', mock_open()) as mock_file:
            with patch('json.dump') as mock_json_dump:
                result = self.highscore_manager.save_highscore()
                self.assertTrue(result)
                mock_file.assert_called_once_with('test_highscore.json', 'w')
                # Check that json.dump was called with the correct data
                args, kwargs = mock_json_dump.call_args
                data = args[0]
                self.assertEqual(data['player_wins'], 15)
                self.assertEqual(data['dealer_wins'], 8)


    def test_update_wins(self):
        """Testar att uppdatera vinster."""
        self.highscore_manager.update_wins(20, 10)
        self.assertEqual(self.highscore_manager.player_wins, 20)
        self.assertEqual(self.highscore_manager.dealer_wins, 10)

    def test_get_scoreboard(self):
        """Testar att hämta poängställningen."""
        self.highscore_manager.player_wins = 3
        self.highscore_manager.dealer_wins = 7
        expected_scoreboard = "Spelare: 3 vinster\nDealern: 7 vinster"
        self.assertEqual(self.highscore_manager.get_scoreboard(), expected_scoreboard)

if __name__ == '__main__':
    unittest.main()
