import os
from pathlib import Path

ROOT = Path(__file__).parent

for c in range(1, 13):
    if c == 1:
        continue
    
    DIR = ROOT / f'Char {c:02}º'
    IMG_DIR = DIR / 'imgs'
    FILE = DIR / '01.py'
    MD = DIR / 'NOTES.md'
    
    os.makedirs(DIR, exist_ok= True)
    os.makedirs(IMG_DIR, exist_ok= True)
    with open(FILE, 'w') as f, open(MD, 'w') as md:
        pass