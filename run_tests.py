#!/usr/bin/env python3
"""
Test runner för att köra alla tester i tests-mappen
"""
import unittest
import sys
import os

def run_all_tests():
    """Kör alla tester i tests-mappen"""
    # Lägg till tests-mappen i sökvägen
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests'))
    
    # Hitta alla testfiler
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    
    # Kör testerna
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    # Returnera exit-kod baserat på resultat
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)