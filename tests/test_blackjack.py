"""
Enhetstester för Blackjack-spelet.
"""
import sys
import os
import unittest
from the_game.card import Card, Deck, Hand, Suit
from the_game.player import Player, Dealer




class TestBlackjack(unittest.TestCase):
    """Testklass för Blackjack-spelet"""
    
    def test_card_value(self):
        """Testar att kortvärden beräknas korrekt"""
        # Testa numeriska kort
        card_7 = Card('7', Suit.HEARTS)
        self.assertEqual(card_7.get_value(), 7)
        
        # Testa knekt, dam, kung
        card_jack = Card('J', Suit.SPADES)
        self.assertEqual(card_jack.get_value(), 10)
        
        # Testa ess
        card_ace = Card('A', Suit.DIAMONDS)
        self.assertEqual(card_ace.get_value(), 11)
    
    def test_hand_aces(self):
        """Testar ess-logik i handen"""
        hand = Hand()
        
        # Testa att ess räknas som 11 när det är bra
        hand.add_card(Card('A', Suit.HEARTS))
        hand.add_card(Card('9', Suit.CLUBS))
        self.assertEqual(hand.get_value(), 20)
        
        # Testa att ess räknas om från 11 till 1 vid överskridande
        hand.add_card(Card('5', Suit.DIAMONDS))  # 20 + 5 = 25, ess måste räknas om
        self.assertEqual(hand.get_value(), 15)  # 9 + 5 + 1 = 15
    
    def test_blackjack_detection(self):
        """Testar Blackjack-identifiering"""
        hand = Hand()
        
        # Lägg till Ess och 10-värdekort för Blackjack
        hand.add_card(Card('A', Suit.HEARTS))
        hand.add_card(Card('K', Suit.SPADES))
        
        self.assertTrue(hand.is_blackjack())
        self.assertEqual(hand.get_value(), 21)
    
    def test_deck_operations(self):
        """Testar kortleksoperationer"""
        deck = Deck()
        initial_count = deck.cards_remaining()
        
        # Testa att dra kort minskar antalet
        card = deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(deck.cards_remaining(), initial_count - 1)
        
        # Testa att blanda decken
        deck.shuffle()
        # Svårt att testa shuffling direkt, men vi kan kontrollera att antalet kort är korrekt
        self.assertEqual(deck.cards_remaining(), initial_count - 1)
    
    def test_dealer_behavior(self):
        """Testar dealerns beteende"""
        # Scenario 1: Dealer should stop at 17
        dealer = Dealer()
        dealer.hand.add_card(Card('10', Suit.DIAMONDS))
        dealer.hand.add_card(Card('6', Suit.CLUBS)) # Hand is 16
        deck = Deck()
        deck.cards = [Card('A', Suit.HEARTS)] # Dealer should draw Ace and stop at 17
        dealer.play_turn(deck)
        self.assertEqual(dealer.hand.get_value(), 17)

        # Scenario 2: Dealer should bust
        dealer = Dealer()
        dealer.hand.add_card(Card('10', Suit.HEARTS))
        dealer.hand.add_card(Card('6', Suit.SPADES)) # Hand is 16
        deck = Deck()
        deck.cards = [Card('8', Suit.CLUBS)] # Dealer should draw 8 and bust
        dealer.play_turn(deck)
        self.assertTrue(dealer.hand.is_bust())


if __name__ == '__main__':
    unittest.main()