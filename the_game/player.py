"""
Spelarmodul för Blackjack-spelet.
Hanterar spelare och dealer.
"""
from .card import Hand, Deck


class Player:
    """Representerar en spelare"""
    
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def reset_hand(self):
        """Återställer spelarens hand"""
        self.hand.clear()
    
    def hit(self, deck):
        """Spelaren drar ett kort"""
        self.hand.add_card(deck.deal_card())
        return self.hand.get_value()
    
    def stand(self):
        """Spelaren stannar"""
        return self.hand.get_value()
    
    def get_stats(self):
        """Returnerar spelarens statistik"""
        return {
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties
        }


class Dealer(Player):
    """Representerar dealern (datorn)"""
    
    def __init__(self):
        super().__init__("Dealer")
    
    def play_turn(self, deck):
        """Dealern spelar sin tur enligt Blackjack-regler"""
        # Dealern måste dra kort tills hen når minst 17
        while self.hand.get_value() < 17:
            self.hit(deck)
            print(f"Dealern drar ett kort. Nuvarande hand: {self.hand}")
        
        return self.hand.get_value()