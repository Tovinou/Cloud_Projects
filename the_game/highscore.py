"""
Highscore-system för Blackjack-spelet.
"""
import json
import os

class Highscore:
    """Hanterar highscore-systemet"""
    
    def __init__(self, filename='highscore.json'):
        self.filename = filename
        self.scores = {}
    
    def load_highscore(self):
        """Laddar highscore från fil"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.scores = json.load(file)
            except (json.JSONDecodeError, IOError):
                self.scores = {}
        else:
            self.scores = {}
    
    def save_highscore(self):
        """Sparar highscore till fil"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.scores, file)
        except IOError:
            print("Kunde inte spara highscore.")
    
    def update_score(self, player_name, result):
        """Uppdaterar poängen för en spelare"""
        if player_name not in self.scores:
            self.scores[player_name] = {'wins': 0, 'losses': 0, 'ties': 0}
        
        if result == 'player':
            self.scores[player_name]['wins'] += 1
        elif result == 'dealer':
            self.scores[player_name]['losses'] += 1
        else:  # tie
            self.scores[player_name]['ties'] += 1
    
    def show_highscore(self):
        """Visar highscore-listan sorterad efter vinstprocent"""
        if not self.scores:
            print("Ingen highscore finns ännu.")
            return
        
        print("\n--- Highscore ---")
        # Sortera spelare efter vinstprocent
        sorted_players = sorted(self.scores.items(), 
                               key=lambda x: (x[1]['wins'] / (x[1]['wins'] + x[1]['losses'] + x[1]['ties'])) 
                               if (x[1]['wins'] + x[1]['losses'] + x[1]['ties']) > 0 else 0, 
                               reverse=True)
        
        for player, stats in sorted_players[:5]:  # Visa top 5
            total_games = stats['wins'] + stats['losses'] + stats['ties']
            if total_games > 0:
                win_percentage = (stats['wins'] / total_games) * 100
                print(f"{player}: {stats['wins']}V/{stats['losses']}F/{stats['ties']}O ({win_percentage:.1f}% vinst)")