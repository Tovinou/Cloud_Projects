import unittest
from unittest.mock import patch, MagicMock
from game.ui import GameUI

class TestGameUI(unittest.TestCase):
    """Testklass för GameUI"""

    @patch('builtins.print')
    def test_show_welcome(self, mock_print):
        """Testar att välkomstmeddelandet skrivs ut korrekt."""
        GameUI.show_welcome()
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call("Välkommen till Tärningsspelet 21!")

    @patch('builtins.print')
    def test_show_round_start(self, mock_print):
        """Testar att rundstart meddelandet skrivs ut korrekt."""
        GameUI.show_round_start(5)
        mock_print.assert_called_once_with("\n" + '🎲' * 10 + " RUNDA 5 " + '🎲' * 10)

    @patch('builtins.print')
    def test_show_dice_roll(self, mock_print):
        """Testar att tärningskast resultat skrivs ut korrekt."""
        GameUI.show_dice_roll("TestPlayer", 6, 15)
        mock_print.assert_called_once_with("TestPlayer slog: 6 (Total: 15)")

    @patch('builtins.print')
    def test_show_bust(self, mock_print):
        """Testar att bust-meddelandet skrivs ut korrekt."""
        GameUI.show_bust("TestPlayer")
        mock_print.assert_called_once_with(" TestPlayer blev tjock! Förlust!")

    @patch('builtins.print')
    def test_show_round_result(self, mock_print):
        """Testar att rundresultatet skrivs ut korrekt."""
        mock_game = MagicMock()
        mock_game.player.__str__.return_value = "Player: 18"
        mock_game.dealer.__str__.return_value = "Dealer: 20"
        GameUI.show_round_result(mock_game)
        self.assertEqual(mock_print.call_count, 5)
        mock_print.assert_any_call("RESULTAT:")
        mock_print.assert_any_call(mock_game.player)
        mock_print.assert_any_call(mock_game.dealer)

    @patch('builtins.print')
    def test_show_winner(self, mock_print):
        """Testar att vinnarmeddelandet skrivs ut korrekt."""
        GameUI.show_winner("player")
        mock_print.assert_called_with(" Spelaren vinner!")
        GameUI.show_winner("dealer")
        mock_print.assert_called_with(" Dealern vinner!")
        GameUI.show_winner("draw")
        mock_print.assert_called_with(" Oavgjort!")

    @patch('builtins.print')
    def test_show_scoreboard(self, mock_print):
        """Testar att poängställningen skrivs ut korrekt."""
        mock_game = MagicMock()
        mock_game.highscore.get_scoreboard.return_value = "Scoreboard"
        GameUI.show_scoreboard(mock_game)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call("STÄLLNING:")
        mock_print.assert_any_call("Scoreboard")

    @patch('builtins.input', side_effect=['j'])
    def test_ask_play_again_yes(self, mock_input):
        """Testar att spela igen med 'j'."""
        self.assertTrue(GameUI.ask_play_again())

    @patch('builtins.input', side_effect=['n'])
    def test_ask_play_again_no(self, mock_input):
        """Testar att inte spela igen med 'n'."""
        self.assertFalse(GameUI.ask_play_again())

    @patch('builtins.input', side_effect=['x', 'ja'])
    @patch('builtins.print')
    def test_ask_play_again_invalid_then_yes(self, mock_print, mock_input):
        """Testar ogiltigt val följt av 'ja'."""
        self.assertTrue(GameUI.ask_play_again())
        mock_print.assert_called_once_with(" Ogiltigt val! Välj 'j' för ja eller 'n' för nej.")

if __name__ == '__main__':
    unittest.main()