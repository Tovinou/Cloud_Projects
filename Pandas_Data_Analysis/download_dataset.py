"""
Download Dataset Script
======================

Detta script laddar ner vgchartz-2024.csv datasetet som behövs för övningarna.
"""

import os
import requests
import pandas as pd
import numpy as np
from pathlib import Path

def download_vgchartz_dataset():
    """Laddar ner vgchartz-2024.csv datasetet."""
    
    # Dataset URL (använd en pålitlig källa)
    dataset_url = "https://raw.githubusercontent.com/GitSquared/node-vgchartz-scraper/master/data/games.csv"
    
    # Alternativt, skapa ett sample dataset baserat på presentationen
    print("=== Laddar ner Dataset för Pandas Övningar ===\n")
    
    try:
        print("Försöker ladda ner dataset från GitHub...")
        response = requests.get(dataset_url, timeout=30)
        
        if response.status_code == 200:
            # Spara datasetet
            with open("vgchartz-2024.csv", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("✓ Dataset laddat ner framgångsrikt från GitHub!")
            
            # Läs in och visa information
            df = pd.read_csv("vgchartz-2024.csv")
            print(f"Dataset innehåller {len(df)} rader och {len(df.columns)} kolumner")
            print("Kolumner:", df.columns.tolist())
            
        else:
            print(f"❌ Kunde inte ladda ner datasetet (HTTP {response.status_code})")
            print("Skapar ett sample dataset istället...")
            create_sample_dataset()
            
    except Exception as e:
        print(f"❌ Fel vid nedladdning: {e}")
        print("Skapar ett sample dataset istället...")
        create_sample_dataset()

def create_sample_dataset():
    """Skapar ett sample dataset som liknar vgchartz-2024.csv."""
    
    print("\nSkapar ett sample dataset för övningarna...")
    
    # Skapa realistisk data baserat på presentationen
    np.random.seed(42)
    n_games = 1000
    
    # Konsoler från presentationen
    consoles = ['PS4', 'Xbox One', 'Switch', 'PC', 'PS5', 'Xbox Series X', '3DS', 'Wii U']
    
    # Genres
    genres = ['Action', 'RPG', 'Sports', 'Adventure', 'Strategy', 'Shooter', 'Racing', 'Puzzle']
    
    # Skapa data
    data = {
        'title': [f'Game_{i}' for i in range(1, n_games + 1)],
        'console': np.random.choice(consoles, n_games),
        'genre': np.random.choice(genres, n_games),
        'total_sales': np.random.uniform(0.1, 50, n_games),
        'na_sales': np.random.uniform(0.1, 25, n_games),
        'eu_sales': np.random.uniform(0.1, 20, n_games),
        'jp_sales': np.random.uniform(0.1, 15, n_games),
        'other_sales': np.random.uniform(0.1, 10, n_games),
        'critics_score': np.random.uniform(0, 10, n_games),
        'user_score': np.random.uniform(0, 10, n_games),
        'year': np.random.randint(2010, 2024, n_games),
        'publisher': np.random.choice(['Nintendo', 'Sony', 'Microsoft', 'EA', 'Ubisoft', 'Activision'], n_games),
        'developer': np.random.choice(['Nintendo', 'Sony', 'Microsoft', 'EA', 'Ubisoft', 'Activision'], n_games)
    }
    
    # Lägg till några kända spel
    known_games = [
        {'title': 'Grand Theft Auto V', 'console': 'PS4', 'total_sales': 23.5, 'critics_score': 9.7},
        {'title': 'Minecraft', 'console': 'PC', 'total_sales': 33.0, 'critics_score': 9.3},
        {'title': 'The Legend of Zelda: Breath of the Wild', 'console': 'Switch', 'total_sales': 29.0, 'critics_score': 9.7},
        {'title': 'Red Dead Redemption 2', 'console': 'PS4', 'total_sales': 46.0, 'critics_score': 9.7},
        {'title': 'FIFA 23', 'console': 'PS4', 'total_sales': 15.0, 'critics_score': 8.2}
    ]
    
    # Ersätt några rader med kända spel
    for i, game in enumerate(known_games):
        if i < len(data['title']):
            data['title'][i] = game['title']
            data['console'][i] = game['console']
            data['total_sales'][i] = game['total_sales']
            data['critics_score'][i] = game['critics_score']
            data['genre'][i] = 'Action' if 'GTA' in game['title'] else 'Adventure'
            data['year'][i] = 2013 if 'GTA' in game['title'] else 2017
    
    # Skapa DataFrame
    df = pd.DataFrame(data)
    
    # Spara som CSV
    df.to_csv("vgchartz-2024.csv", index=False)
    print("✓ Sample dataset skapat och sparat som 'vgchartz-2024.csv'")
    print(f"Dataset innehåller {len(df)} rader och {len(df.columns)} kolumner")
    
    # Visa de första raderna
    print("\nDe första 5 raderna:")
    print(df.head())
    
    # Visa information om datasetet
    print("\nDataset information:")
    print(df.info())
    
    return df

def verify_dataset():
    """Verifierar att datasetet finns och kan läsas."""
    
    if os.path.exists("vgchartz-2024.csv"):
        try:
            df = pd.read_csv("vgchartz-2024.csv")
            print(f"\n✓ Dataset verifierat: {len(df)} rader, {len(df.columns)} kolumner")
            print("Kolumner:", df.columns.tolist())
            return True
        except Exception as e:
            print(f"❌ Fel vid läsning av datasetet: {e}")
            return False
    else:
        print("❌ Datasetet 'vgchartz-2024.csv' finns inte")
        return False

if __name__ == "__main__":
    print("=== Dataset Downloader för Pandas Övningar ===\n")
    
    # Försök ladda ner datasetet
    download_vgchartz_dataset()
    
    # Verifiera datasetet
    if verify_dataset():
        print("\n🎉 Datasetet är redo för övningarna!")
        print("Du kan nu köra: python pandas_exercises.py")
    else:
        print("\n❌ Problem med datasetet. Kontrollera filen och försök igen.")

