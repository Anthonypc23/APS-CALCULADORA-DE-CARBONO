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
            # Se vazio, considera como 0
            if v == "" or v is None:
                novos_valores[k] = 0.0
            else:
                v_float = float(v)
                if v_float >= 0:
                    novos_valores[k] = v_float
                else:
                    return None
        except ValueError:
            return None
    return novos_valores

# Calculo de emissões (ANUAL)
def calc_eletricidade(consumo_mensal):
    # Consumo mensal * 12 meses
    return consumo_mensal * 12 * carregajson("eletricidade/kwh")

def calc_combustivel(consumo_diario):
    # Consumo diário * 365 dias
    return consumo_diario * 365 * carregajson("combustivel/litro")

def calc_voo(distancia_mensal):
    # Distância mensal * 12 meses
    return distancia_mensal * 12 * carregajson("voo/km")

def calc_Transporte(distancia_diaria):
    # Distância diária * 365 dias
    return distancia_diaria * 365 * carregajson("Transporte")

def calc_gas_natural(consumo_mensal):
    # Consumo mensal * 12 meses
    return consumo_mensal * 12 * carregajson("gas_natural/m3")

def calc_agua(consumo_mensal):
    # Consumo mensal * 12 meses
    return consumo_mensal * 12 * carregajson("agua/m3")

def calc_residuos(consumo_mensal):
    # Consumo mensal * 12 meses
    return consumo_mensal * 12 * carregajson("residuos/kg")

def calc_alimentacao_carne(consumo_semanal):
    # Converte consumo semanal para mensal (4.33 semanas/mês)
    return consumo_semanal * 4.33 * carregajson("carne/kg")

def calc_alimentacao_vegetariana(refeicoes_semanais):
    # Converte refeições semanais para mensal
    return refeicoes_semanais * 4.33 * carregajson("vegetariano/refeicao")

def calc_credito(entradas):
    
    total_emissao = 0
    valor = {}

    # Cálculos básicos
    total_emissao += calc_eletricidade(entradas['eletricidade'])
    total_emissao += calc_combustivel(entradas['combustivel'])
    total_emissao += calc_Transporte(entradas['transporte'])
    total_emissao += calc_voo(entradas['voo'])

    valor['eletricidade'] = calc_eletricidade(entradas['eletricidade'])
    valor['combustivel'] = calc_combustivel(entradas['combustivel'])
    valor['Transporte'] = calc_Transporte(entradas['transporte'])
    valor['voo'] = calc_voo(entradas['voo'])
    
    # Novos cálculos
    if 'gas_natural' in entradas:
        gas = calc_gas_natural(entradas['gas_natural'])
        total_emissao += gas
        valor['gas_natural'] = gas
    
    if 'agua' in entradas:
        agua = calc_agua(entradas['agua'])
        total_emissao += agua
        valor['agua'] = agua
    
    if 'residuos' in entradas:
        residuos = calc_residuos(entradas['residuos'])
        total_emissao += residuos
        valor['residuos'] = residuos
    
    if 'carne' in entradas:
        carne = calc_alimentacao_carne(entradas['carne'])
        total_emissao += carne
        valor['carne'] = carne
    
    if 'vegetariano' in entradas:
        veg = calc_alimentacao_vegetariana(entradas['vegetariano'])
        total_emissao += veg
        valor['vegetariano'] = veg
    
    # Total em toneladas
    valor['total'] = total_emissao / 1000
    
    # Sistema de compensação
    import math
    valor['creditos'] = math.ceil(valor['total'])  # Arredonda para cima
    valor['arvores'] = math.ceil(total_emissao / carregajson("arvore_absorcao_kg"))
    valor['valor_compensacao'] = valor['creditos'] * carregajson("preco_credito_rs")
    
    print(valor)
    return valor