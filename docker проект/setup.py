from setuptools import setup

setup(
    name="levenshtein_cli",
    version="0.1.0",
    description="CLI для вычисления расстояния Левенштейна между строками",
    author="Владислав",
    author_email="you@example.com",
    py_modules=["levenshtein_cli"],  # берём одиночный модуль levenshtein_cli.py
    entry_points={
        'console_scripts': [
            'levenshtein=levenshtein_cli:main',
        ],
    },
    install_requires=[],  
    python_requires='>=3.6',
)
