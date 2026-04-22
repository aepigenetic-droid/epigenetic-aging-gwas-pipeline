import os
from pathlib import Path

def create_structure():
    folders = [
        "data/raw",
        "data/interim",
        "data/processed",
        "outputs/logs",
        "outputs/figures",
        "outputs/ldsc",
        "refs/ldsc",
        "refs/baselineLD",
        "refs/hm3",
    ]

    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"Created: {folder}")

if __name__ == "__main__":
    create_structure()
