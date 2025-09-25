import random

class Player:
    """Klass för att representera en spelare (både human och dealer)"""
    
    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer
        self.score = 0
        self.wins = 0
        self.is_busted = False
    
    def roll_dice(self):
        """Slår tärningen och lägger till värdet till spelarens poäng"""
        roll = random.randint(1, 6)
        self.score += roll
        return roll
    
    def reset_round(self):
        """Återställer spelarens poäng för en ny runda"""
        self.score = 0
        self.is_busted = False
    
    def __str__(self):
        return f"{self.name}: {self.score} poäng"