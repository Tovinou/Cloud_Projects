"""
Huvudspellogik för Blackjack-spelet.
"""
import os
from .card import Deck
from .player import Player, Dealer
from .highscore import Highscore


class Game:
    """Hanterar spelets huvudlogik"""
    
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Spelare")
        self.dealer = Dealer()
        self.highscore = Highscore()
    
    def display_hands(self, show_dealer_hand=True):
        """Visar spelarens och dealerns händer"""
        print(f"\n{self.player.name}: {self.player.hand}")
        
        if show_dealer_hand:
            print(f"{self.dealer.name}: {self.dealer.hand}")
        else:
            # Visa bara dealerns första kort och dölj det andra
            if len(self.dealer.hand.cards) >= 2:
                first_card = str(self.dealer.hand.cards[0])
                print(f"{self.dealer.name}: {first_card} [dolt kort]")
            elif self.dealer.hand.cards:
                first_card = str(self.dealer.hand.cards[0])
                print(f"{self.dealer.name}: {first_card}")
    
    def player_turn(self):
        """Hanterar spelarens tur"""
        while True:
            self.display_hands(show_dealer_hand=False)
            
            if self.player.hand.is_bust():
                print("Du har blivit tjock! Dealern vinner.")
                return False
            
            if self.player.hand.is_blackjack():
                print("Blackjack! Du vinner!")
                return True
            
            # Varna spelaren om hen har hög poäng
            current_score = self.player.hand.get_value()
            if current_score >= 17:
                print(f"Du har {current_score} poäng - hög risk att bli tjock om du drar!")
            
            choice = input("\nVill du [d]ra ett kort eller [s]tanna? ").lower().strip()
            
            if choice == 'd':
                self.player.hit(self.deck)
                new_card = self.player.hand.cards[-1]
                print(f"Du drar ett kort: {new_card}")
                
            elif choice == 's':
                print("Du väljer att stanna.")
                return True
            else:
                print("Ogiltigt val. Välj 'd' för att dra eller 's' för att stanna.")
    
    def dealer_turn(self):
        """Hanterar dealerns tur"""
        print("\n--- Dealerns tur ---")
        self.display_hands(show_dealer_hand=True)
        
        if self.dealer.hand.is_blackjack():
            print("Dealern har Blackjack!")
            return False
        
        self.dealer.play_turn(self.deck)
        
        if self.dealer.hand.is_bust():
            print("Dealern har blivit tjock! Du vinner!")
            return True
        
        return None  # Ingen har blivit tjock, jämför poäng
    
    def determine_winner(self):
        """Avgör vinnaren baserat på poängen"""
        player_value = self.player.hand.get_value()
        dealer_value = self.dealer.hand.get_value()
        
        print(f"\n--- Resultat ---")
        print(f"Dina poäng: {player_value}")
        print(f"Dealerns poäng: {dealer_value}")
        
        if player_value > dealer_value:
            print("Grattis! Du vinner!")
            return 'player'
        elif dealer_value > player_value:
            print("Dealern vinner!")
            return 'dealer'
        else:
            print("Oavgjort!")
            return 'tie'
    
    def update_stats(self, result):
        """Uppdaterar spelstatistiken"""
        if result == 'player':
            self.player.wins += 1
            self.dealer.losses += 1
        elif result == 'dealer':
            self.player.losses += 1
            self.dealer.wins += 1
        else:  # tie
            self.player.ties += 1
            self.dealer.ties += 1
        
        # Uppdatera highscore
        self.highscore.update_score(self.player.name, result)
    
    def play_round(self):
        """Spelar en omgång Blackjack"""
        print("\n" + "="*50)
        print("NY OMGÅNG BLACKJACK")
        print("="*50)
        
        # Återställ händer
        self.player.reset_hand()
        self.dealer.reset_hand()
        
        # Dela ut två kort till varje spelare
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)
        
        print("Korten har delats ut!")
        
        # Spelarens tur
        player_result = self.player_turn()
        
        if not player_result:  # Spelaren blev tjock
            self.update_stats('dealer')
            return
        
        if player_result is True and not self.player.hand.is_blackjack():
            # Dealerns tur (om spelaren inte redan vunnit med blackjack)
            dealer_result = self.dealer_turn()
            
            if dealer_result is True:  # Dealern blev tjock
                self.update_stats('player')
                return
            elif dealer_result is False:  # Dealern fick blackjack
                self.update_stats('dealer')
                return
        
        # Ingen blev tjock, jämför poäng
        result = self.determine_winner()
        self.update_stats(result)
    
    def show_stats(self):
        """Visar aktuell statistik"""
        print(f"\n--- Statistik ---")
        print(f"{self.player.name}: {self.player.wins} vinster, {self.player.losses} förluster, {self.player.ties} oavgjorda")
        print(f"{self.dealer.name}: {self.dealer.wins} vinster, {self.dealer.losses} förluster, {self.dealer.ties} oavgjorda")
        
        # Beräkna vinstprocent
        total_games = self.player.wins + self.player.losses + self.player.ties
        if total_games > 0:
            win_percentage = (self.player.wins / total_games) * 100
            print(f"Vinstprocent: {win_percentage:.1f}%")
        
        # Visa highscore
        self.highscore.show_highscore()
    
    def run(self):
        """Huvudloop för spelet"""
        print("Välkommen till Blackjack!")
        print("\nRegler:")
        print("- Försök komma närmare 21 än dealern utan att överskrida 21")
        print("- Ess kan vara 1 eller 11 poäng")
        print("- Knekt, Dam, Kung är värda 10 poäng")
        print("- Dealern måste dra kort tills hen når minst 17 poäng")
        print("- Blackjack (Ess + 10-poängskort) vinner direkt!")
        print("- Om du överskrider 21 poäng 'blir du tjock' och förlorar")
        
        # Ladda highscore
        self.highscore.load_highscore()
        
        while True:
            self.play_round()
            self.show_stats()
            
            play_again = input("\nVill du spela igen? (j/n): ").lower().strip()
            if play_again != 'j':
                print("Tack för spelet!")
                # Spara highscore när spelet avslutas
                self.highscore.save_highscore()
                break