"""
Test Setup Script
================

Detta script testar att alla nödvändiga paket kan importeras utan fel.
"""

def test_imports():
    """Testar att alla paket kan importeras."""
    try:
        print("Testar imports...")
        
        import pandas as pd
        print("✓ pandas importerat")
        
        import numpy as np
        print("✓ numpy importerat")
        
        import matplotlib.pyplot as plt
        print("✓ matplotlib importerat")
        
        import seaborn as sns
        print("✓ seaborn importerat")
        
        import requests
        print("✓ requests importerat")
        
        try:
            import kaggle
            print("✓ kaggle importerat")
        except Exception as e:
            print(f"⚠ kaggle inte konfigurerat: {e}")
            print("   (Detta är inte kritiskt för övningarna)")
        
        print("\n🎉 Alla grundläggande paket fungerar!")
        return True
        
    except Exception as e:
        print(f"❌ Fel vid import: {e}")
        return False

def test_basic_pandas():
    """Testar grundläggande Pandas-funktionalitet."""
    try:
        import pandas as pd
        import numpy as np
        
        print("\nTestar Pandas...")
        
        # Skapa en enkel DataFrame
        data = {
            'title': ['Game 1', 'Game 2', 'Game 3'],
            'console': ['PS4', 'PC', 'Switch'],
            'sales': [10.5, 5.2, 8.7]
        }
        
        df = pd.DataFrame(data)
        print("✓ DataFrame skapad")
        
        # Testa head()
        print("\nTestar head(2):")
        print(df.head(2))
        
        print("✓ Pandas fungerar korrekt!")
        return True
        
    except Exception as e:
        print(f"❌ Fel vid Pandas-test: {e}")
        return False

if __name__ == "__main__":
    print("=== Test Setup Script ===\n")
    
    # Testa imports
    if test_imports():
        # Testa Pandas
        test_basic_pandas()
        
        print("\n🎉 Alla tester godkända!")
        print("Du kan nu köra: python simple_exercises.py")
        print("Eller: python kaggle_dataset_setup.py (utan Kaggle)")
    else:
        print("\n❌ Vissa paket saknas. Installera med: pip install -r requirements.txt")
