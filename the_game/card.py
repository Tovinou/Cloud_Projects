"""
Kortmodul för Blackjack-spelet.
Hanterar kort, kortlek och kortdragning.
"""
import random
from enum import Enum


class Suit(Enum):
    """Kortfärger"""
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"


class Card:
    """Representerar ett spelkort"""
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def get_value(self):
        """Returnerar kortets värde enligt Blackjack-regler"""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Ess kan vara 1 eller 11, hanteras i Hand-klassen
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank}{self.suit.value}"


class Deck:
    """Representerar en kortlek"""
    
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        """Skapar en komplett kortlek"""
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = list(Suit)
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        """Blandar kortleken"""
        random.shuffle(self.cards)
    
    def deal_card(self):
        """Drar ett kort från leken"""
        if len(self.cards) == 0:
            # Om kortleken är tom, skapa en ny och blanda
            self.create_deck()
            self.shuffle()
        return self.cards.pop()
    
    def cards_remaining(self):
        """Returnerar antal kort kvar i leken"""
        return len(self.cards)


class Hand:
    """Representerar en spelares hand"""
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        """Lägger till ett kort i handen"""
        self.cards.append(card)
        self.value += card.get_value()
        
        # Räkna ess
        if card.rank == 'A':
            self.aces += 1
        
        # Justera för ess (11 -> 1 om värdet blir över 21)
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def get_value(self):
        """Returnerar handens totala värde"""
        return self.value
    
    def is_bust(self):
        """Kontrollerar om handen har gått över 21"""
        return self.value > 21
    
    def is_blackjack(self):
        """Kontrollerar om handen är blackjack (21 med 2 kort)"""
        return len(self.cards) == 2 and self.value == 21
    
    def clear(self):
        """Tömmer handen"""
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def __str__(self):
        cards_str = " ".join(str(card) for card in self.cards)
        return f"{cards_str} (värde: {self.value})"