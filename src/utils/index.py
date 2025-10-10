import json
from pathlib import Path

file = Path("src/Data/fatores.json")

def carregajson(file):

    if file.exists():

        with open(file,"r", encoding="utf-8") as f:
            fator = json.load(f)
            print(fator)
            return fator
    else:
        print("fatores nãoo declarados")


