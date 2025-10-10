# BDD Bookstore Project

## Lösningsbeskrivning

Denna lösning implementerar ett enkelt bokhandelssystem med BDD (Behavior-Driven Development) med Gherkin och Behave.

### Valda extrafunktioner

Jag valde följande tre extrafunktioner:

1. **Rabattfunktion** - Ger 10% rabatt när kunden köper 4 eller fler böcker
2. **Lagerhantering** - Förhindrar att kunder köper fler böcker än vad som finns i lager
3. **Login-system** - Kräver inloggning för att genomföra köp

### Anledningar till valet

- **Rabattfunktion**: Bra för att testa beräkningar och edge cases
- **Lagerhantering**: Viktig real-world funktionalitet med komplex logik
- **Login-system**: Grundläggande för många webbapplikationer, bra för att testa flöden

### Implementeringsdetaljer

- Använde Python-klasser för att simulera domänmodeller
- Separerade steps i olika filer för bättre organisation
- Använde Scenario Outline för att testa multiple cases
- Implementerade proper error handling

### Vad som var lätt

- Strukturera Gherkin-scenarier
- Skapa grundläggande step definitions
- Implementera enkel varukorgslogik

### Vad som var utmanande

- Hantera state mellan olika steps
- Implementera lagerreservationer
- Skapa meningsfulla error messages
- Hantera edge cases som negativa kvantiteter

### Resurser för Del 2

- Behave dokumentation: https://behave.readthedocs.io/
- Gherkin reference: https://cucumber.io/docs/gherkin/
- Python unit testing patterns
- BDD best practices artiklar

## Köra testen

```bash
# Installera behave
pip install behave

# Kör alla test
behave

# Kör test med specifika taggar
behave --tags=shopping_cart
behave --tags=discount
behave --tags=inventory
behave --tags=login
```

## Miljö och körning

- Rekommenderat: kör i virtuell miljö (valfritt namn `.venv`):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install behave
```

- På Windows PowerShell: använd separata kommandon (inte `&&`).
  Exempel:

```powershell
cd bookstore_bdd
behave
```

## Projektstruktur (kort)

- `features/*.feature`: Gherkin-scenarier (`discount.feature`, `inventory.feature`, `login.feature`, `shopping_cart.feature`)
- `features/steps/*.py`: Stegdefinitioner uppdelade per domän
- `models/*.py`: Domänmodeller (`Book`, `Inventory`, `ShoppingCart`, `User`)
- `features/environment.py`: Delad kontext/init (om tillämpligt)

## Viktiga implementationdetaljer

- Lagerbegränsningar och felmeddelanden:
  - Vid försök att överskrida lagersaldo svarar `Inventory.reserve_book(...)` med
    "Only X copy/copies available" (matchar krav i feature-filerna).
  - "Out of stock" returneras när saldo är 0.
- Steg med tabeller som saknar `Author` hanteras: vi sätter författare till "Unknown Author" i sådana fall.
- Kolon i stegtexter: feature-rader som slutar med `:` har motsvarande stegdefinitioner med `:` (t.ex. `Given the following inventory:`) för att undvika mismatch.

## Felsökning

- AmbiguousStep: Kontrollera att samma stegtext inte är definierad i flera steg-filer. Ta bort dubbletter eller förena till en enda implementation.
- Undefined steps: Säkerställ att stegtext (inklusive kolon och parametrar) exakt matchar mellan `.feature` och `steps/*.py`.
- PowerShell-parsing: Använd separata kommandon istället för `&&`.

## Exempel på körning

```powershell
# Från projektroten
cd bookstore_bdd
behave
```