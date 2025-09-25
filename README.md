# Tärningsspelet 21 (Dice Game 21)

Ett enkelt tärningsspel där målet är att komma så nära 21 som möjligt utan att gå över.

## Beskrivning

Tärningsspelet 21 är ett turbaserat spel där spelaren och dealern turas om att slå en tärning. Varje tärningskast adderas till spelarens poäng. Målet är att komma så nära 21 som möjligt utan att bli "tjock" (gå över 21).

### Spelregler

1. Spelaren börjar och väljer att slå tärningen eller stanna
2. Om spelaren slår över 21 blir hen "tjock" och förlorar automatiskt
3. Om spelaren stannar, är det dealerns tur
4. Dealern slår automatiskt tills den når minst 17 poäng
5. Den som kommer närmast 21 utan att gå över vinner
6. Om båda går över 21 blir det oavgjort
7. Om båda har samma poäng blir det oavgjort

## Installation

1. Klona detta repository:
   ```
   git clone https://github.com/yourusername/twenty_1_game.git
   cd twenty_1_game
   ```

2. Skapa en virtuell miljö (rekommenderas):
   ```
   python -m venv env
   ```

3. Aktivera den virtuella miljön:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`

4. Installera beroenden:
   ```
   pip install -r requirements.txt
   ```

## Användning

Starta spelet genom att köra:
```
python main.py
```

Följ instruktionerna på skärmen för att spela. Du kommer att få välja mellan att slå tärningen (`r`) eller stanna (`s`) under din tur.

## Projektstruktur

```
twenty_1_game/
├── game/                   # Spelmoduler
│   ├── __init__.py
│   ├── game_logic.py       # Spellogik
│   ├── highscore.py        # Poänghantering
│   ├── player.py           # Spelarklasser
│   └── ui.py               # Användargränssnitt
├── tests/                  # Testmoduler
│   ├── __init__.py
│   ├── test_dealer_ai.py
│   ├── test_game_logic.py
│   ├── test_integration.py
│   └── test_player.py
├── .gitignore
├── main.py                 # Huvudprogram
├── README.md
├── requirements.txt
└── run_tests.py            # Kör alla tester
```

## Tester

Kör alla tester med:
```
python run_tests.py
```

Eller använd pytest direkt:
```
pytest
```

För att se kodtäckning:
```
pytest --cov=game
```

## Utveckling

För att bidra till projektet:

1. Skapa en fork av projektet
2. Skapa en feature branch: `git checkout -b feature/amazing-feature`
3. Gör dina ändringar och commit: `git commit -m 'Add amazing feature'`
4. Push till din branch: `git push origin feature/amazing-feature`
5. Öppna en Pull Request

## Licens

Detta projekt är licensierat under MIT-licensen - se [LICENSE](LICENSE) filen för detaljer.