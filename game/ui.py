class GameUI:
    """Hanterar användargränssnittet för spelet"""
    
    @staticmethod
    def show_welcome():
        """Visar välkomstmeddelande"""
        print("Välkommen till Tärningsspelet 21!")
        print("Målet är att komma närmast 21 utan att bli tjock (>21).")
        print("-" * 50)
    
    @staticmethod
    def show_round_start(round_number):
        """Visar rundstart"""
        print(f"\n{'🎲' * 10} RUNDA {round_number} {'🎲' * 10}")
    
    @staticmethod
    def show_dice_roll(player_name, roll, total_score):
        """Visar tärningskast resultat"""
        print(f"{player_name} slog: {roll} (Total: {total_score})")
    
    @staticmethod
    def show_bust(player_name):
        """Visar bust-meddelande"""
        print(f" {player_name} blev tjock! Förlust!")
    
    @staticmethod
    def show_round_result(game):
        """Visar rundans resultat"""
        print("\n" + "="*40)
        print("RESULTAT:")
        print(game.player)
        print(game.dealer)
        print("="*40)
    
    @staticmethod
    def show_winner(result):
        """Visar vinnaren"""
        if result == "player":
            print(" Spelaren vinner!")
        elif result == "dealer":
            print(" Dealern vinner!")
        else:
            print(" Oavgjort!")
    
    @staticmethod
    def show_scoreboard(game):
        """Visar ställning"""
        print("\n" + "="*40)
        print("STÄLLNING:")
        print(game.highscore.get_scoreboard())
        print("="*40)
    
    @staticmethod
    def ask_play_again():
        """Frågar om att spela igen"""
        while True:
            try:
                choice = input("\nVill du spela igen? [j]a/[n]ej: ").lower().strip()
                if choice in ['j', 'ja', 'y', 'yes']:
                    return True
                elif choice in ['n', 'nej', 'no']:
                    return False
                else:
                    print(" Ogiltigt val! Välj 'j' för ja eller 'n' för nej.")
            except (KeyboardInterrupt, EOFError):
                return False
            except Exception:
                continue