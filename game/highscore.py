import json
import os
from datetime import datetime

class HighscoreManager:
    """Hanterar highscore-funktionalitet"""
    
    def __init__(self, filename="highscore.json"):
        self.filename = filename
        self.player_wins = 0
        self.dealer_wins = 0
    
    def load_highscore(self):
        """Laddar highscore från fil om den finns"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.player_wins = data.get('player_wins', 0)
                    self.dealer_wins = data.get('dealer_wins', 0)
                return True
            return False
        except Exception as e:
            print(f"Fel vid laddning av highscore: {e}")
            return False
    
    def save_highscore(self):
        """Sparar highscore till fil"""
        try:
            data = {
                'player_wins': self.player_wins,
                'dealer_wins': self.dealer_wins,
                'last_updated': datetime.now().isoformat()
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Fel vid sparning av highscore: {e}")
            return False
    
    def update_wins(self, player_wins, dealer_wins):
        """Uppdaterar vinststatistik"""
        self.player_wins = player_wins
        self.dealer_wins = dealer_wins
    
    def get_scoreboard(self):
        """Returnerar aktuell ställning som en sträng"""
        return f"Spelare: {self.player_wins} vinster\nDealern: {self.dealer_wins} vinster"