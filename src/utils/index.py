import json
import os.path

path = "src/data/fatores.json"

def carregajson(search):
    if not os.path.exists(path):
        raise FileNotFoundError(f"O arquivo {path} não foi encontrado.")
    with open(path, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        return dados.get(search)

# Tratamento de dados
def tratar_dados(valores):
    novos_valores = {}
    for k, v in valores.items():
        try:
            v_float = float(v)
            if v_float >= 0:
                novos_valores[k] = v_float
            else:
                return None
        except ValueError:
            return None
    return novos_valores

# Calculo de emissões
def calc_eletricidade(consumo_mensal):
    return consumo_mensal * carregajson("eletricidade/kwh")

def calc_combustivel(consumo_mensal):
    return consumo_mensal * carregajson("combustivel/litro")

def calc_voo(distancia):
    return distancia * carregajson("voo/km")

def calc_credito(entradas):
    total_emissao = 0

    total_emissao += calc_eletricidade(entradas['eletricidade'])
    total_emissao += calc_combustivel(entradas['combustivel'])
    total_emissao += calc_voo(entradas['voo'])

    return total_emissao / carregajson("credito/ton")