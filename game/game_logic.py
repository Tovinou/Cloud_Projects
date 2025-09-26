from .player import Player
from .highscore import HighscoreManager

class Game21:
    """Huvudklass för spelets logik"""
    
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Player("Dealern", is_dealer=True)
        self.highscore = HighscoreManager()
        self.highscore.load_highscore()
        self.player.wins = self.highscore.player_wins
        self.dealer.wins = self.highscore.dealer_wins
    
    def player_turn(self):
        """Hanterar spelarens tur - returnerar True om tur är klar, False om avbruten"""
        while True:
            try:
                choice = input("Vill du [r]ulla eller [s]tanna? ").lower().strip()
            except KeyboardInterrupt:
                return False
            except Exception:
                continue
            
            if choice in ['r', 'rulla']:
                roll = self.player.roll_dice()
                print(f"Du slog: {roll}. Total poäng: {self.player.score}")
                
                if self.player.score > 21:
                    self.player.is_busted = True
                    print("Du blev tjock! (över 21)")
                    return True
                elif self.player.score == 21:
                    print("Du fick 21! Perfekt!")
                    return True
                    
            elif choice in ['s', 'stanna']:
                return True
            else:
                print(" Ogiltigt val! Välj 'r' för rulla eller 's' för stanna.")
    
    def dealer_turn(self):
        """Hanterar dealerns tur (automatisk enligt regler)"""
        while self.dealer.score < 17:
            self.dealer.roll_dice()
            if self.dealer.score > 21:
                self.dealer.is_busted = True
                return
    
    def determine_winner(self):
        """Bestämmer vinnaren av rundan"""
        if self.player.is_busted and self.dealer.is_busted:
            return "draw"
        elif self.player.is_busted:
            self.dealer.wins += 1
            return "dealer"
        elif self.dealer.is_busted:
            self.player.wins += 1
            return "player"
        else:
            player_diff = 21 - self.player.score
            dealer_diff = 21 - self.dealer.score
            
            if player_diff < dealer_diff:
                self.player.wins += 1
                return "player"
            elif dealer_diff < player_diff:
                self.dealer.wins += 1
                return "dealer"
            else:
                return "draw"
    
    def play_round(self):
        """Spelar en hel runda"""
        self.player.reset_round()
        self.dealer.reset_round()
        
        if not self.player_turn():
            return False  # Spelaren avbröt
        
        if not self.player.is_busted:
            self.dealer_turn()
        
        result = self.determine_winner()
        
        # Uppdatera highscore
        self.highscore.update_wins(self.player.wins, self.dealer.wins)
        self.highscore.save_highscore()
        
        return result
    
    def reset_game(self):
        """Återställer hela spelet"""
        self.player.wins = 0
        self.dealer.wins = 0
        self.highscore.update_wins(0, 0)
        self.highscore.save_highscore()