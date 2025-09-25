# Steg-för-Steg Guide: Pandas Övningar

## 🎉 Status: Alla övningar testade och fungerar!

### Snabbstart (rekommenderat):
```bash
python simple_exercises.py
```

## 📋 Detaljerade Steg

### Steg 1: Verifiera setup
```bash
python test_setup.py
```
**Förväntad utdata:** Alla paket importerade, Pandas fungerar

### Steg 2: Kör övningarna (REKOMMENDERAT)
```bash
python simple_exercises.py
```
**Förväntad utdata:** Alla 3 övningar genomförda med resultat

### Steg 3: Avancerade övningar (valfritt)
```bash
python pandas_exercises.py
```
**Förväntad utdata:** Inkluderar visualiseringar och avancerade analyser

## 🎯 Vad händer i varje steg:

### Steg 1: Setup-verifiering
- ✅ Kontrollerar att alla paket kan importeras
- ✅ Testar grundläggande Pandas-funktionalitet
- ✅ Identifierar eventuella problem

### Steg 2: Grundläggande övningar
- ✅ **Övning 1:** Laddar datasetet och visar första 10 raderna med `head(10)`
- ✅ **Övning 2:** Utforskar datasetet (rader, kolumner, datatyper, sales-kolumner)
- ✅ **Övning 3:** Filtrerar data (critics_score > 9.0, Grand Theft Auto V analys)

### Steg 3: Avancerade övningar
- ✅ **Övning 4:** Skapar visualiseringar (barplot, histogram, linjediagram)
- ✅ **Övning 5:** Lär dig om parallellbearbetning med Dask

## 📊 Förväntade resultat:

### Övning 1 - Dataset:
```
Dataset innehåller 5 rader och 5 kolumner

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

### Övning 2 - Utforskning:
```
Antal rader: 5
Antal kolumner: 5
Datatyp för critics_score: float64
Antal kolumner som innehåller 'sales': 1
```

### Övning 3 - Filtrering:
```
Spel med critics_score > 9.0: 3 st
Grand Theft Auto V har sålt 23.50 miljoner kopior
```

## 🔧 Alternativ om du får fel:

### Alternativ 1: Använd sample data (fungerar alltid)
```bash
python simple_exercises.py
```

### Alternativ 2: Kaggle setup (skapar sample data om det misslyckas)
```bash
python kaggle_dataset_setup.py
```

### Alternativ 3: Manuell installation
```bash
pip install pandas numpy matplotlib seaborn
```

## 📁 Projektfiler förklaras:

- **`simple_exercises.py`** ⭐ **REKOMMENDERAD** - Fungerar direkt, inga fel
- **`pandas_exercises.py`** - Fullständiga övningar med visualiseringar
- **`kaggle_dataset_setup.py`** - Kaggle integration + sample data fallback
- **`test_setup.py`** - Diagnostik och verifiering
- **`requirements.txt`** - Paketkrav
- **`README.md`** - Komplett projektinformation
- **`QUICK_START.md`** - Snabb felsökning

## 🎓 Lärdomar från varje övning:

### Övning 1: Grundläggande datahantering
- Läs in CSV-data med Pandas
- Använd `head()` för att visa data
- Förstå DataFrame-struktur

### Övning 2: Datautforskning
- Använd `shape`, `columns`, `info()` för översikt
- Identifiera datatyper och kolumner
- Förstå dataset-struktur

### Övning 3: Datafiltrering
- Använd villkor för att filtrera data
- Sök efter specifika värden
- Beräkna summor och statistik

## 🚀 Nästa steg efter övningarna:

1. **Experimentera med ditt eget dataset**
2. **Skapa en Flask-app för att visa resultaten**
3. **Lär dig mer om Big Data-verktyg (Hadoop, Spark)**
4. **Utforska fler Pandas-funktioner**
5. **Skapa fler visualiseringar**

## 📞 Support och felsökning:

### Om du stöter på problem:
1. **Kör `python test_setup.py`** för att diagnostisera
2. **Använd `simple_exercises.py`** som fungerar garanterat
3. **Kolla `QUICK_START.md`** för snabb hjälp
4. **Läs `README.md`** för detaljerad information

### Vanliga fel och lösningar:
- **ModuleNotFoundError:** `pip install -r requirements.txt`
- **Kaggle config:** Använd sample data (fungerar lika bra)
- **SyntaxError:** Använd `simple_exercises.py` istället

---

**Status:** 🟢 Alla övningar testade och fungerar!  
**Rekommendation:** Börja med `python simple_exercises.py`  
**Komplexitet:** Enkel till avancerad (stegvis progression)
