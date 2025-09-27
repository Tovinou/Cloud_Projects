from setuptools import setup, find_packages

setup(
    name="blackjack_spel",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  # Tom eftersom vi bara använder standardbibliotek
    entry_points={
        'console_scripts': [
            'blackjack=the_game.main:main',
        ],
    },
    author="Komlan",
    description="Ett textbaserat Blackjack-spel",
    python_requires='>=3.6',
)