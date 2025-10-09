import json
from pathlib import Path

file = Path("src/Data/fatores.json")

if file.exists():

    with open(file,"r", encoding="utf-8") as f:
        fator = json.load(f)
    print(fator)
else:
    print("fatores nãoo declarados")
