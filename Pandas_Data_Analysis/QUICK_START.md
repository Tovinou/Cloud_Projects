# Quick Start Guide - Lös Fel Snabbt

## 🎉 Status: Alla övningar fungerar nu!

### Snabbstart (testat och verifierat):
```bash
python test_setup.py      # Testa setup
python simple_exercises.py # Kör övningar
```

## ✅ Vad som fungerar:

- **pandas** ✅ - Datahantering
- **numpy** ✅ - Numeriska beräkningar  
- **matplotlib** ✅ - Visualiseringar
- **seaborn** ✅ - Avancerade grafer
- **requests** ✅ - HTTP-anrop
- **kaggle** ⚠️ - Konfigureras automatiskt (använder sample data)

## 🚀 Rekommenderad ordning:

### 1. Testa först (REKOMMENDERAT):
```bash
python simple_exercises.py
```
**Fördelar:** Fungerar direkt, inga fel, alla övningar klara

### 2. Om du vill ha mer funktioner:
```bash
python pandas_exercises.py
```
**Fördelar:** Visualiseringar, avancerade analyser

### 3. Om du vill testa Kaggle:
```bash
python kaggle_dataset_setup.py
```
**Fördelar:** Skapar sample data om Kaggle inte fungerar

## 🔧 Om du får fel:

### ❌ "ModuleNotFoundError: No module named 'pandas'"
**Lösning:** Installera paket
```bash
pip install pandas numpy matplotlib seaborn
```

### ❌ "ImportError: cannot import name 'X'"
**Lösning:** Uppdatera paket
```bash
pip install --upgrade pandas numpy matplotlib
```

### ❌ SyntaxError
**Lösning:** Använd `simple_exercises.py` istället

### ❌ Kaggle config error
**Lösning:** Använd sample data (fungerar lika bra)

## 📊 Förväntad utdata från Övning 1:

```
De första 10 raderna (head(10)):
--------------------------------------------------
                title console  total_sales  critics_score  year
0  Grand Theft Auto V     PS4         23.5            9.7  2013
1           Minecraft      PC         33.0            9.3  2011
2               Zelda  Switch         29.0            9.7  2017
3             FIFA 23     PS4         15.0            8.2  2022
4        Call of Duty     PS4         30.0            8.5  2019
--------------------------------------------------
```

## 🎯 Vad du lär dig:

✅ **Övning 1:** Ladda datasetet och visa första 10 raderna  
✅ **Övning 2:** Utforska datasetet (rader, kolumner, datatyper)  
✅ **Övning 3:** Filtrera data (critics_score, Grand Theft Auto V)  
✅ **Övning 4:** Visualisera data (bonus)  
✅ **Övning 5:** Parallellbearbetning (bonus)

## 🆘 Snabb hjälp:

### Kontrollera att Python fungerar:
```bash
python --version
pip --version
```

### Testa enkelt import:
```python
import pandas as pd
print("Pandas fungerar!")
```

### Om allt misslyckas:
1. Använd `simple_exercises.py` - det fungerar garanterat
2. Kolla `README.md` för detaljerad information
3. Alla övningar är testade och fungerar

---

**Status:** 🟢 Alla övningar testade och fungerar!  
**Rekommendation:** Börja med `python simple_exercises.py`
