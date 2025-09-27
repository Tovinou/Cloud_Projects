# Blackjack Spel

Ett textbaserat Blackjack-spel implementerat i Python.

## Beskrivning

Detta är en klassisk version av kortspelet Blackjack (även känt som 21) där du spelar mot en automatiserad dealer. Spelet är byggt med Python och körs i terminalen. Målet är att få en hand med ett totalt värde närmare 21 än dealerns hand, utan att överskrida 21.

## Funktioner

- Spela flera omgångar av Blackjack mot en dealer.
- Dra kort ("hit") eller stanna ("stand").
- Automatisk beräkning av handens värde, inklusive korrekt hantering av Ess.
- System för att spåra vinster, förluster och oavgjorda matcher.
- En lokal highscore-lista som sparar resultat mellan spelsessioner.
- Enkla och tydliga regler som visas vid start.

## Krav

- Python 3.6 eller senare.

## Installation

För att säkerställa att alla importvägar fungerar korrekt för både spelet och testerna rekommenderas det att installera projektet i "editable mode".

1.  **Klona eller ladda ner projektet.**
2.  **Navigera till projektets rotmapp** i din terminal.
3.  **Kör följande kommando** för att installera projektet:
    ```bash
    pip install -e .
    ```

## Hur man spelar

För att starta spelet, se till att du är i projektets rotmapp (`C:\Jensen\python\Blackjack_spel`) och kör följande kommando:

```bash
python run.py
```

Följ sedan instruktionerna på skärmen för att spela.

## Hur man kör testerna

Projektet innehåller enhetstester för att verifiera spelets logik. För att köra testerna, se till att du är i projektets rotmapp och kör följande kommando:

```bash
python -m unittest discover
```
