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

# Tratamento de dados
def trata_numero(valor):
    try:
        valor = float(valor)
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        return valor
    except ValueError:
        raise ValueError("Entrada inválida. Por favor, insira um número válido.")

# Calculo de emissões
def calc_eletricidade(consumo_mensal):
    return consumo_mensal * carregajson(file)["eletricidade/kwh"]

def calc_combustivel(consumo_mensal):
    return consumo_mensal * carregajson(file)["combustivel/litro"]

def calc_voo(distancia):
    return distancia * carregajson(file)["voo/km"]

def calc_credito(entradas):
    total_emissao = 0

    total_emissao += calc_eletricidade(entradas['eletricidade'])
    total_emissao += calc_combustivel(entradas['combustivel'])
    total_emissao += calc_voo(entradas['voo'])

    return total_emissao / carregajson(file)["credito/ton"]