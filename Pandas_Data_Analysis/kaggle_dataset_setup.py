"""
Kaggle Dataset Setup för Pandas Övningar
========================================

Detta script hjälper dig att:
1. Ladda ner vgchartz-2024.csv från Kaggle
2. Läs in det i en Pandas DataFrame
3. Visa de första 10 raderna med head(10)
"""

import os
import pandas as pd
import numpy as np

def check_kaggle_installation():
    """Kontrollerar om Kaggle CLI är installerat."""
    try:
        import kaggle
        print("✓ Kaggle API installerat")
        return True
    except ImportError:
        print("❌ Kaggle API inte installerat")
        print("Installera med: pip install kaggle")
        return False
    except Exception as e:
        print(f"⚠ Kaggle API inte konfigurerat: {e}")
        print("   (Skapar sample dataset istället)")
        return False

def download_from_kaggle():
    """Försöker ladda ner datasetet från Kaggle."""
    try:
        import kaggle
        print("Försöker ladda ner vgchartz-2024.csv från Kaggle...")
        
        # Sök efter dataset
        try:
            datasets = kaggle.api.dataset_list(search="vgchartz")
            if datasets:
                print(f"Hittade {len(datasets)} dataset med 'vgchartz'")
                for ds in datasets[:3]:  # Visa första 3
                    print(f"- {ds.ref}: {ds.title}")
        except Exception as e:
            print(f"Kunde inte söka efter dataset: {e}")
        
        # Försök ladda ner specifikt dataset
        try:
            kaggle.api.dataset_download_files("vgchartz/video-game-sales", path=".", unzip=True)
            print("✓ Dataset laddat ner från Kaggle!")
            return True
        except Exception as e:
            print(f"Kunde inte ladda ner från Kaggle: {e}")
            return False
            
    except Exception as e:
        print(f"Fel vid Kaggle-nedladdning: {e}")
        return False

def create_realistic_sample_dataset():
    """Skapar ett realistiskt sample dataset baserat på vgchartz-format."""
    
    print("\nSkapar ett realistiskt sample dataset...")
    
    # Skapa data baserat på riktiga speldata
    np.random.seed(42)
    n_games = 1000
    
    # Konsoler och genres
    consoles = ['PS4', 'Xbox One', 'Switch', 'PC', 'PS5', 'Xbox Series X', '3DS', 'Wii U']
    genres = ['Action', 'RPG', 'Sports', 'Adventure', 'Strategy', 'Shooter', 'Racing', 'Puzzle']
    
    # Skapa realistisk data
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
    
    # Lägg till kända spel från presentationen
    known_games = [
        {'title': 'Grand Theft Auto V', 'console': 'PS4', 'total_sales': 23.5, 'critics_score': 9.7, 'year': 2013},
        {'title': 'Minecraft', 'console': 'PC', 'total_sales': 33.0, 'critics_score': 9.3, 'year': 2011},
        {'title': 'The Legend of Zelda: Breath of the Wild', 'console': 'Switch', 'total_sales': 29.0, 'critics_score': 9.7, 'year': 2017},
        {'title': 'Red Dead Redemption 2', 'console': 'PS4', 'total_sales': 46.0, 'critics_score': 9.7, 'year': 2018},
        {'title': 'FIFA 23', 'console': 'PS4', 'total_sales': 15.0, 'critics_score': 8.2, 'year': 2022},
        {'title': 'Call of Duty: Modern Warfare', 'console': 'PS4', 'total_sales': 30.0, 'critics_score': 8.5, 'year': 2019},
        {'title': 'Super Mario Odyssey', 'console': 'Switch', 'total_sales': 25.0, 'critics_score': 9.7, 'year': 2017},
        {'title': 'God of War', 'console': 'PS4', 'total_sales': 23.0, 'critics_score': 9.4, 'year': 2018},
        {'title': 'Spider-Man', 'console': 'PS4', 'total_sales': 20.0, 'critics_score': 8.7, 'year': 2018},
        {'title': 'Animal Crossing: New Horizons', 'console': 'Switch', 'total_sales': 42.0, 'critics_score': 9.0, 'year': 2020}
    ]
    
    # Ersätt första raderna med kända spel
    for i, game in enumerate(known_games):
        if i < len(data['title']):
            data['title'][i] = game['title']
            data['console'][i] = game['console']
            data['total_sales'][i] = game['total_sales']
            data['critics_score'][i] = game['critics_score']
            data['year'][i] = game['year']
            data['genre'][i] = 'Action' if 'GTA' in game['title'] or 'Call of Duty' in game['title'] else 'Adventure'
            data['publisher'][i] = 'Rockstar' if 'GTA' in game['title'] else 'Nintendo' if 'Nintendo' in game['title'] else 'Sony'
    
    # Skapa DataFrame
    df = pd.DataFrame(data)
    
    # Spara som CSV
    df.to_csv("vgchartz-2024.csv", index=False)
    print("✓ Sample dataset skapat och sparat som 'vgchartz-2024.csv'")
    print(f"Dataset innehåller {len(df)} rader och {len(df.columns)} kolumner")
    
    return df

def run_exercise_1():
    """Kör Övning 1: Ladda datasetet och visa första 10 raderna."""
    
    print("\n" + "="*60)
    print("ÖVNING 1: Ladda datasetet")
    print("="*60)
    
    # Kontrollera om datasetet finns
    if os.path.exists("vgchartz-2024.csv"):
        print("✓ Dataset 'vgchartz-2024.csv' hittades!")
        df = pd.read_csv("vgchartz-2024.csv")
    else:
        print("❌ Dataset 'vgchartz-2024.csv' hittades inte!")
        print("Skapar ett sample dataset...")
        df = create_realistic_sample_dataset()
    
    print(f"\nDataset innehåller {len(df)} rader och {len(df.columns)} kolumner")
    
    # Visa de första 10 raderna med head(10) som specificerat i presentationen
    print("\nDe första 10 raderna (head(10)):")
    print("-" * 80)
    print(df.head(10))
    print("-" * 80)
    
    # Visa dataset information
    print("\nDataset information:")
    print(f"Form: {df.shape}")
    print(f"Kolumner: {df.columns.tolist()}")
    
    return df

def main():
    """Huvudfunktion som kör hela setup-processen."""
    
    print("=== Kaggle Dataset Setup för Pandas Övningar ===\n")
    
    # Försök ladda ner från Kaggle först
    if check_kaggle_installation():
        if download_from_kaggle():
            print("✓ Dataset laddat ner från Kaggle!")
        else:
            print("Skapar sample dataset istället...")
            create_realistic_sample_dataset()
    else:
        print("Skapar sample dataset...")
        create_realistic_sample_dataset()
    
    # Kör Övning 1
    df = run_exercise_1()
    
    print("\n🎉 Setup komplett!")
    print("Du kan nu köra: python pandas_exercises.py")
    print("Eller fortsätt med övningarna direkt i denna session.")

if __name__ == "__main__":
    main()
