"""
Enkel Pandas Övningar - Utan fel
=================================

Detta är en förenklad version av övningarna som ska fungera direkt.
"""

import pandas as pd
import numpy as np

def create_sample_dataset():
    """Skapar ett enkelt sample dataset."""
    print("Skapar sample dataset...")
    
    # Skapa enkelt data
    data = {
        'title': ['Grand Theft Auto V', 'Minecraft', 'Zelda', 'FIFA 23', 'Call of Duty'],
        'console': ['PS4', 'PC', 'Switch', 'PS4', 'PS4'],
        'total_sales': [23.5, 33.0, 29.0, 15.0, 30.0],
        'critics_score': [9.7, 9.3, 9.7, 8.2, 8.5],
        'year': [2013, 2011, 2017, 2022, 2019]
    }
    
    df = pd.DataFrame(data)
    return df

def exercise_1():
    """Övning 1: Ladda datasetet och visa första 10 raderna."""
    print("=" * 50)
    print("ÖVNING 1: Ladda datasetet")
    print("=" * 50)
    
    # Skapa dataset
    df = create_sample_dataset()
    
    print(f"Dataset innehåller {len(df)} rader och {len(df.columns)} kolumner")
    
    # Visa de första 10 raderna med head(10) - exakt som specificerat
    print("\nDe första 10 raderna (head(10)):")
    print("-" * 50)
    print(df.head(10))
    print("-" * 50)
    
    return df

def exercise_2():
    """Övning 2: Utforska datasetet."""
    print("\n" + "=" * 50)
    print("ÖVNING 2: Utforska datasetet")
    print("=" * 50)
    
    df = create_sample_dataset()
    
    print(f"Antal rader: {df.shape[0]}")
    print(f"Antal kolumner: {df.shape[1]}")
    
    if 'critics_score' in df.columns:
        print(f"Datatyp för critics_score: {df['critics_score'].dtype}")
    
    sales_columns = [col for col in df.columns if 'sales' in col]
    print(f"Antal kolumner som innehåller 'sales': {len(sales_columns)}")
    
    print("\nDataset information:")
    print(df.info())
    
    return df

def exercise_3():
    """Övning 3: Filtrera data."""
    print("\n" + "=" * 50)
    print("ÖVNING 3: Filtrera data")
    print("=" * 50)
    
    df = create_sample_dataset()
    
    # Filtrera spel med critics_score > 9.0
    high_score_games = df[df['critics_score'] > 9.0]
    print(f"Spel med critics_score > 9.0: {len(high_score_games)} st")
    
    if len(high_score_games) > 0:
        print("Dessa spel:")
        print(high_score_games[['title', 'total_sales', 'console', 'critics_score']])
    
    # Hitta Grand Theft Auto V
    gta_games = df[df['title'].str.contains('Grand Theft Auto V', case=False, na=False)]
    if len(gta_games) > 0:
        total_sales = gta_games['total_sales'].sum()
        print(f"\nGrand Theft Auto V har sålt {total_sales:.2f} miljoner kopior")
    
    return df

def main():
    """Huvudfunktion som kör alla övningar."""
    print("=== Enkla Pandas Övningar ===\n")
    
    try:
        # Kör alla övningar
        df1 = exercise_1()
        df2 = exercise_2()
        df3 = exercise_3()
        
        print("\n🎉 Alla övningar genomförda!")
        print("Du kan nu skapa ditt eget dataset eller fortsätta med visualiseringar.")
        
    except Exception as e:
        print(f"❌ Ett fel uppstod: {e}")
        print("Kontrollera att alla paket är installerade.")

if __name__ == "__main__":
    main()
