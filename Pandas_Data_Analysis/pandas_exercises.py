"""
Dataanalys i Python med Pandas - Övningar
==========================================

Detta script innehåller alla övningar från presentationen om Big Data och dataanalys.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=== Dataanalys i Python med Pandas - Övningar ===\n")
    
    # Övning 1: Ladda datasetet
    print("1. Laddar datasetet...")
    try:
        # Försök läsa in datasetet (användaren måste ladda ner det först)
        df = pd.read_csv("vgchartz-2024.csv")
        print("✓ Dataset laddat framgångsrikt!")
        print(f"Dataset innehåller {len(df)} rader och {len(df.columns)} kolumner\n")
        
        # Visa de första 10 raderna
        print("De första 10 raderna:")
        print(df.head(10))
        print()
        
    except FileNotFoundError:
        print("❌ Dataset 'vgchartz-2024.csv' hittades inte!")
        print("Ladda ner datasetet från Kaggle först.")
        print("Du kan skapa en sample dataset för att testa koden.\n")
        
        # Skapa en sample dataset för demonstration
        print("Skapar ett sample dataset för demonstration...")
        df = create_sample_dataset()
        print("✓ Sample dataset skapat!\n")
    
    # Övning 2: Utforska datasetet
    print("2. Utforskar datasetet...")
    explore_dataset(df)
    
    # Övning 3: Filtrera data
    print("3. Filtrerar data...")
    filter_data(df)
    
    # Övning 4: Visualisera data (bonus)
    print("4. Visualiserar data...")
    visualize_data(df)
    
    # Övning 5: Parallellbearbetning med Dask (bonus)
    print("5. Parallellbearbetning...")
    parallel_processing_demo()

def create_sample_dataset():
    """Skapar ett sample dataset för demonstration om det riktiga datasetet inte finns."""
    np.random.seed(42)
    
    # Skapa sample data
    n_games = 1000
    consoles = ['PS4', 'Xbox One', 'Switch', 'PC', 'PS5']
    genres = ['Action', 'RPG', 'Sports', 'Adventure', 'Strategy']
    
    data = {
        'title': [f'Game_{i}' for i in range(1, n_games + 1)],
        'console': np.random.choice(consoles, n_games),
        'genre': np.random.choice(genres, n_games),
        'total_sales': np.random.uniform(0.1, 50, n_games),
        'critics_score': np.random.uniform(0, 10, n_games),
        'user_score': np.random.uniform(0, 10, n_games),
        'year': np.random.randint(2010, 2024, n_games)
    }
    
    return pd.DataFrame(data)

def explore_dataset(df):
    """Utforskar datasetet enligt övning 2."""
    print(f"Antal rader: {df.shape[0]}")
    print(f"Antal kolumner: {df.shape[1]}")
    
    # Hitta critics_score kolumnen
    if 'critics_score' in df.columns:
        print(f"Datatyp för critics_score: {df['critics_score'].dtype}")
    else:
        print("Kolumnen 'critics_score' finns inte i datasetet")
    
    # Räkna kolumner som innehåller '_sales'
    sales_columns = [col for col in df.columns if '_sales' in col]
    print(f"Antal kolumner som innehåller '_sales': {len(sales_columns)}")
    if sales_columns:
        print(f"Sales-kolumner: {sales_columns}")
    
    print("\nDataset information:")
    print(df.info())
    
    print("\nStatistisk sammanfattning:")
    print(df.describe())
    
    print("\nKolumner:")
    print(df.columns.tolist())
    print()

def filter_data(df):
    """Filtrerar data enligt övning 3."""
    # Filtrera spel med critics_score > 9.9
    if 'critics_score' in df.columns:
        high_score_games = df[df['critics_score'] > 9.9]
        print(f"Spel med critics_score > 9.9: {len(high_score_games)} st")
        
        if len(high_score_games) > 0:
            print("Dessa spel:")
            display_cols = ['title', 'total_sales', 'console', 'critics_score']
            available_cols = [col for col in display_cols if col in df.columns]
            print(high_score_games[available_cols].head(10))
        else:
            print("Inga spel hittades med så hög score.")
    else:
        print("Kolumnen 'critics_score' finns inte i datasetet")
    
    print()
    
    # Beräkna försäljning för Grand Theft Auto V
    if 'title' in df.columns and 'total_sales' in df.columns:
        gta_games = df[df['title'].str.contains('Grand Theft Auto V', case=False, na=False)]
        if len(gta_games) > 0:
            total_sales = gta_games['total_sales'].sum()
            print(f"Grand Theft Auto V har sålt {total_sales:.2f} miljoner kopior")
        else:
            print("Grand Theft Auto V hittades inte i datasetet")
    else:
        print("Krävda kolumner för GTA-analys saknas")
    
    print()

def visualize_data(df):
    """Visualiserar data enligt övning 4."""
    try:
        # Skapa en figur med flera subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Dataanalys av Speldataset', fontsize=16)
        
        # 1. Försäljning per konsol (barplot)
        if 'console' in df.columns and 'total_sales' in df.columns:
            sales_per_console = df.groupby('console')['total_sales'].sum()
            sales_per_console = sales_per_console.sort_values(ascending=False)
            
            axes[0, 0].bar(range(len(sales_per_console)), sales_per_console.values)
            axes[0, 0].set_title('Total försäljning per konsol')
            axes[0, 0].set_xlabel('Konsol')
            axes[0, 0].set_ylabel('Försäljning (miljoner)')
            axes[0, 0].set_xticks(range(len(sales_per_console)))
            axes[0, 0].set_xticklabels(sales_per_console.index, rotation=45)
        
        # 2. Fördelning av försäljning (histogram)
        if 'total_sales' in df.columns:
            axes[0, 1].hist(df['total_sales'].dropna(), bins=30, alpha=0.7, edgecolor='black')
            axes[0, 1].set_title('Fördelning av försäljning')
            axes[0, 1].set_xlabel('Försäljning (miljoner)')
            axes[0, 1].set_ylabel('Antal spel')
        
        # 3. Försäljning över tid (linjediagram)
        if 'year' in df.columns and 'total_sales' in df.columns:
            yearly_sales = df.groupby('year')['total_sales'].sum()
            axes[1, 0].plot(yearly_sales.index, yearly_sales.values, marker='o')
            axes[1, 0].set_title('Försäljning över tid')
            axes[1, 0].set_xlabel('År')
            axes[1, 0].set_ylabel('Total försäljning (miljoner)')
            axes[1, 0].tick_params(axis='x', rotation=45)
        
        # 4. Top 10 mest sålda spel
        if 'title' in df.columns and 'total_sales' in df.columns:
            top_games = df.nlargest(10, 'total_sales')[['title', 'total_sales']]
            axes[1, 1].barh(range(len(top_games)), top_games['total_sales'])
            axes[1, 1].set_title('Top 10 mest sålda spel')
            axes[1, 1].set_xlabel('Försäljning (miljoner)')
            axes[1, 1].set_yticks(range(len(top_games)))
            axes[1, 1].set_yticklabels(top_games['title'], fontsize=8)
        
        plt.tight_layout()
        plt.savefig('spel_analys.png', dpi=300, bbox_inches='tight')
        print("✓ Visualiseringar skapade och sparade som 'spel_analys.png'")
        
        # Visa graferna
        plt.show()
        
    except Exception as e:
        print(f"❌ Fel vid visualisering: {e}")
        print("Kontrollera att matplotlib är installerat och att datasetet har rätt format.")

def parallel_processing_demo():
    """Demonstrerar parallellbearbetning med Dask (bonus övning)."""
    print("Parallellbearbetning med Dask:")
    print("Dask kan hantera större mängder data genom att dela upp dem i mindre bitar")
    print("och bearbeta dem parallellt.")
    print()
    print("För att använda Dask:")
    print("1. Installera: pip install dask[complete]")
    print("2. Importera: import dask.dataframe as dd")
    print("3. Läs data: ddf = dd.read_csv('fil.csv')")
    print("4. Bearbeta: result = ddf.groupby('kolumn').sum().compute()")
    print()
    print("Dask skalar bättre än Pandas vid Big Data och kräver installation av dask-modulen.")

if __name__ == "__main__":
    main()
