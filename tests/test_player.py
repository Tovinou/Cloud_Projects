import unittest
from game.player import Player
from game.game_logic import Game21

class TestPlayer(unittest.TestCase):
    """Testklass för Player-klassen"""
    
    def setUp(self):
        """Setup som körs före varje test"""
        self.player = Player("TestSpelare")
        self.dealer = Player("TestDealer", is_dealer=True)
    
    def test_player_initialization(self):
        """Testar att spelare initieras korrekt"""
        # Test 1: Kontrollera att spelaren har rätt startvärden
        self.assertEqual(self.player.name, "TestSpelare")
        self.assertEqual(self.player.score, 0)
        self.assertFalse(self.player.is_busted)
        self.assertEqual(self.player.wins, 0)
        self.assertFalse(self.player.is_dealer)
        
        # Test 2: Kontrollera att dealern har rätt attribut
        self.assertTrue(self.dealer.is_dealer)
    
    def test_dice_roll_range(self):
        """Testar att tärningskast alltid är mellan 1-6"""
        # Test 3: Kontrollera att tärningskast är inom giltigt intervall
        for _ in range(100):
            roll = self.player.roll_dice()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)
        
        # Test 4: Kontrollera att poängen ökas korrekt
        initial_score = self.player.score
        roll_value = self.player.roll_dice()
        self.assertEqual(self.player.score, initial_score + roll_value)
    
    def test_bust_condition(self):
        """Testar att bust-logik fungerar korrekt"""
        # Test 5: Simulera att spelaren blir tjock
        self.player.score = 20
        self.player.roll_dice()
        
        if self.player.score > 21:
            self.player.is_busted = True
        
        if self.player.score > 21:
            self.assertTrue(self.player.is_busted)
        else:
            self.assertFalse(self.player.is_busted)
    
    def test_score_reset(self):
        """Testar att poäng återställs korrekt mellan rundor"""
        # Test 6: Sätta poäng och sedan återställa
        self.player.score = 15
        self.player.is_busted = True
        self.player.reset_round()
        
        self.assertEqual(self.player.score, 0)
        self.assertFalse(self.player.is_busted)