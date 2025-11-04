# 4. DESENVOLVIMENTO DO SISTEMA

## 4.1. Arquitetura do Sistema

### 4.1.1. Visão Geral da Arquitetura

A aplicação foi desenvolvida seguindo uma arquitetura em camadas, adaptando o padrão MVC (Model-View-Controller) para o contexto de uma aplicação desktop Python. Esta escolha arquitetural proporciona separação clara de responsabilidades, facilitando manutenção, testes e possíveis extensões futuras (FOWLER, 2002).

A arquitetura é composta por três camadas principais:

**Camada de Apresentação (View)**: Responsável pela interface gráfica e interação com o usuário. Implementada no módulo `view/index.py`, utiliza CustomTkinter para criar uma interface moderna e intuitiva.

**Camada de Lógica de Negócio (Controller/Utils)**: Contém as regras de negócio, cálculos de emissões e processamento de dados. Implementada no módulo `utils/index.py`, esta camada é independente da interface, permitindo reutilização e testes isolados.

**Camada de Dados (Model)**: Armazena fatores de emissão e configurações em formato JSON. O arquivo `data/fatores.json` serve como base de dados simples, facilmente editável e versionável.

### 4.1.2. Fluxo de Dados

O fluxo de dados na aplicação segue o seguinte padrão:

1. **Entrada de Dados**: Usuário insere valores de consumo através da interface gráfica.

2. **Validação**: Dados são validados pela função `tratar_dados()`, que verifica tipos, valores negativos e campos vazios.

3. **Cálculo**: Dados validados são processados por funções específicas de cálculo (`calc_eletricidade()`, `calc_combustivel()`, etc.).

4. **Agregação**: Função `calc_credito()` agrega resultados individuais e calcula métricas adicionais (créditos, árvores, custo).

5. **Apresentação**: Resultados são formatados e exibidos na interface através de labels, janelas de relatório ou sistema de compensação.

### 4.1.3. Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────┐
│                     main.py                             │
│                  (Entry Point)                          │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  view/index.py                          │
│              (Interface Gráfica)                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ - Janela Principal                               │  │
│  │ - Campos de Entrada                              │  │
│  │ - Botões de Ação                                 │  │
│  │ - Janela de Relatório                            │  │
│  │ - Janela de Compensação                          │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                 utils/index.py                          │
│              (Lógica de Negócio)                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ - tratar_dados()                                 │  │
│  │ - calc_eletricidade()                            │  │
│  │ - calc_combustivel()                             │  │
│  │ - calc_voo()                                     │  │
│  │ - calc_Transporte()                              │  │
│  │ - calc_gas_natural()                             │  │
│  │ - calc_agua()                                    │  │
│  │ - calc_residuos()                                │  │
│  │ - calc_credito()                                 │  │
│  │ - carregajson()                                  │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              data/fatores.json                          │
│               (Dados Persistentes)                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │ - Fatores de Emissão                             │  │
│  │ - Parâmetros de Compensação                      │  │
│  │ - Ações de Compensação                           │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

## 4.2. Modelagem de Dados

### 4.2.1. Estrutura do Arquivo JSON

O arquivo `fatores.json` armazena todos os dados necessários para os cálculos. Sua estrutura foi projetada para ser intuitiva e facilmente extensível:

```json
{
    "eletricidade/kwh": 0.038,
    "combustivel/litro": 2.3477,
    "voo/km": 0.123,
    "Transporte": 0.017,
    "gas_natural/m3": 1.95,
    "agua/m3": 0.15,
    "residuos/kg": 0.5,
    "credito/ton": 1000,
    "arvore_absorcao_kg": 21.77,
    "preco_credito_rs": 50,
    "compensacao": {
        "plantar_arvore": {
            "nome": "Plantar Árvores",
            "reducao_kg_ano": 21.77,
            "descricao": "..."
        },
        ...
    }
}
```

**Justificativa da Estrutura**:
- Chaves descritivas facilitam compreensão
- Valores numéricos diretos simplificam cálculos
- Objeto `compensacao` aninhado organiza dados relacionados
- Formato permite fácil adição de novos fatores

### 4.2.2. Modelo de Dados de Entrada

Dados de entrada do usuário são estruturados como dicionário Python:

```python
{
    "eletricidade": float,    # kWh/mês
    "combustivel": float,     # L/dia
    "voo": float,            # km/mês
    "transporte": float,     # km/dia
    "gas_natural": float,    # m³/mês
    "agua": float,           # m³/mês
    "residuos": float        # kg/mês
}
```

### 4.2.3. Modelo de Dados de Saída

Resultados dos cálculos são retornados como dicionário estruturado:

```python
{
    "eletricidade": float,        # kg CO₂/ano
    "combustivel": float,         # kg CO₂/ano
    "voo": float,                # kg CO₂/ano
    "Transporte": float,         # kg CO₂/ano
    "gas_natural": float,        # kg CO₂/ano
    "agua": float,               # kg CO₂/ano
    "residuos": float,           # kg CO₂/ano
    "total": float,              # toneladas CO₂/ano
    "creditos": int,             # créditos necessários
    "arvores": int,              # árvores para plantar
    "valor_compensacao": float   # R$ estimado
}
```

## 4.3. Módulo de Cálculos (utils/index.py)

### 4.3.1. Função de Carregamento de Dados

```python
def carregajson(search):
    if not os.path.exists(path):
        raise FileNotFoundError(f"O arquivo {path} não foi encontrado.")
    with open(path, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        return dados.get(search)
```

Esta função centraliza o acesso aos fatores de emissão, implementando:
- Verificação de existência do arquivo
- Tratamento de encoding UTF-8 para caracteres especiais
- Retorno seguro com `.get()` para evitar KeyError

### 4.3.2. Função de Tratamento de Dados

```python
def tratar_dados(valores):
    novos_valores = {}
    for k, v in valores.items():
        try:
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
```

**Funcionalidades Implementadas**:
- Conversão de strings para float
- Tratamento de campos vazios como zero
- Rejeição de valores negativos
- Retorno de None em caso de erro (sinaliza entrada inválida)

**Justificativa**: Esta abordagem permite que usuários deixem campos vazios sem causar erros, melhorando usabilidade.

### 4.3.3. Funções de Cálculo por Categoria

Cada categoria de emissão possui função dedicada que aplica fator de emissão e multiplica por período anual:

**Eletricidade** (mensal → anual):
```python
def calc_eletricidade(consumo_mensal):
    # Consumo mensal * 12 meses * fator de emissão
    return consumo_mensal * 12 * carregajson("eletricidade/kwh")
```

**Combustível** (diário → anual):
```python
def calc_combustivel(consumo_diario):
    # Consumo diário * 365 dias * fator de emissão
    return consumo_diario * 365 * carregajson("combustivel/litro")
```

**Viagens Aéreas** (mensal → anual):
```python
def calc_voo(distancia_mensal):
    # Distância mensal * 12 meses * fator de emissão
    return distancia_mensal * 12 * carregajson("voo/km")
```

**Transporte Público** (diário → anual):
```python
def calc_Transporte(distancia_diaria):
    # Distância diária * 365 dias * fator de emissão
    return distancia_diaria * 365 * carregajson("Transporte")
```

**Gás Natural** (mensal → anual):
```python
def calc_gas_natural(consumo_mensal):
    # Consumo mensal * 12 meses * fator de emissão
    return consumo_mensal * 12 * carregajson("gas_natural/m3")
```

**Água** (mensal → anual):
```python
def calc_agua(consumo_mensal):
    # Consumo mensal * 12 meses * fator de emissão
    return consumo_mensal * 12 * carregajson("agua/m3")
```

**Resíduos** (mensal → anual):
```python
def calc_residuos(consumo_mensal):
    # Consumo mensal * 12 meses * fator de emissão
    return consumo_mensal * 12 * carregajson("residuos/kg")
```

**Padrão de Design**: Todas as funções seguem mesmo padrão:
1. Recebem valor no período original (dia ou mês)
2. Convertem para período anual (× 365 ou × 12)
3. Aplicam fator de emissão
4. Retornam kg CO₂/ano

### 4.3.4. Função de Agregação e Compensação

```python
def calc_credito(entradas):
    total_emissao = 0
    valor = {}

    # Calcula emissões por categoria
    valor['eletricidade'] = calc_eletricidade(entradas['eletricidade'])
    valor['combustivel'] = calc_combustivel(entradas['combustivel'])
    valor['Transporte'] = calc_Transporte(entradas['transporte'])
    valor['voo'] = calc_voo(entradas['voo'])
    
    # Soma emissões básicas
    total_emissao += valor['eletricidade']
    total_emissao += valor['combustivel']
    total_emissao += valor['Transporte']
    total_emissao += valor['voo']
    
    # Adiciona categorias opcionais se presentes
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
    
    # Converte para toneladas
    valor['total'] = total_emissao / 1000
    
    # Calcula métricas de compensação
    import math
    valor['creditos'] = math.ceil(valor['total'])
    valor['arvores'] = math.ceil(total_emissao / carregajson("arvore_absorcao_kg"))
    valor['valor_compensacao'] = valor['creditos'] * carregajson("preco_credito_rs")
    
    return valor
```

**Funcionalidades**:
- Agrega emissões de todas as categorias
- Converte kg para toneladas
- Calcula créditos necessários (arredonda para cima)
- Estima árvores necessárias
- Calcula custo de compensação

**Uso de math.ceil()**: Garante que número de créditos e árvores seja sempre suficiente para compensar totalmente as emissões.

## 4.4. Interface Gráfica (view/index.py)

### 4.4.1. Configuração Inicial

```python
import customtkinter as ctk
from utils.index import calc_credito, tratar_dados

ctk.set_appearance_mode('dark')  # Modo escuro por padrão

app = ctk.CTk()
app.title("Calculadora de Carbono - Neutralidade Climática")
app.geometry('1600x900')
app.grid_columnconfigure((0,1,2,3,4), weight=1)
```

**Decisões de Design**:
- Modo escuro reduz fadiga visual
- Dimensões 1600x900 acomodam confortavelmente todos os elementos
- Grid com 5 colunas permite layout flexível

### 4.4.2. Cabeçalho da Aplicação

```python
frameHeader = ctk.CTkFrame(app, fg_color="#1f6aa5", corner_radius=15)
frameHeader.grid(row=0, column=0, columnspan=5, sticky="ew", padx=20, pady=20)

labelH1 = ctk.CTkLabel(frameHeader, text="CALCULADORA DE EMISSÕES DE CO2", 
                       font=("Arial", 38, "bold"), text_color="white")
labelH1.pack(pady=15)

labelSubtitulo = ctk.CTkLabel(frameHeader, text="Calcule sua pegada de carbono e descubra como compensar", 
                              font=("Arial", 16), text_color="#e0e0e0")
labelSubtitulo.pack(pady=(0, 15))
```

**Elementos de Design**:
- Cor azul (#1f6aa5) transmite confiança e profissionalismo
- Bordas arredondadas (corner_radius=15) modernizam visual
- Hierarquia tipográfica clara (38pt bold para título, 16pt para subtítulo)

### 4.4.3. Frame de Entrada de Dados

```python
frameInputs = ctk.CTkFrame(app, fg_color="#2b2b2b", corner_radius=15)
frameInputs.grid(row=1, column=0, columnspan=5, sticky="ew", padx=20, pady=10)
frameInputs.grid_columnconfigure((0,1,2,3,4), weight=1)

ctk.CTkLabel(frameInputs, text="DADOS DE CONSUMO", font=("Arial", 20, "bold"), 
             text_color="#1f6aa5").grid(row=0, column=0, columnspan=5, pady=15)
```

**Organização dos Campos**:
- Primeira linha: 5 campos principais (Eletricidade, Gasolina, Avião, Transporte, Gás)
- Segunda linha: 2 campos centralizados (Água, Resíduos)
- Labels descritivos com unidades claras
- Placeholders "0" indicam formato esperado

**Exemplo de Campo**:
```python
labelEletro = ctk.CTkLabel(frameInputs, text="Eletricidade\n(kWh/Mês)", 
                           font=("Arial", 13, "bold"), justify="center")
labelEletro.grid(row=1, column=0, padx=10, pady=10)

entryEletro = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                           font=("Arial", 14), justify="center")
entryEletro.grid(row=2, column=0, padx=10, pady=5)
```

### 4.4.4. Frame de Resultado

```python
frameResultado = ctk.CTkFrame(app, fg_color="#1a472a", corner_radius=15)
frameResultado.grid(row=2, column=0, columnspan=5, sticky="ew", padx=20, pady=20)

labelTituloResultado = ctk.CTkLabel(frameResultado, text="TOTAL DE EMISSÕES ANUAIS", 
                                    font=("Arial", 24, "bold"), text_color="white")
labelTituloResultado.pack(pady=(20, 10))

labelResultado = ctk.CTkLabel(frameResultado, text="0.00 toneladas de CO2/ano", 
                              font=("Arial", 36, "bold"), text_color="#90ee90")
labelResultado.pack(pady=(0, 20))
```

**Escolhas de Cor**:
- Verde escuro (#1a472a) associado a sustentabilidade
- Texto verde claro (#90ee90) para valores, indicando resultado positivo (conscientização)

### 4.4.5. Botões de Ação

```python
frameBotoes = ctk.CTkFrame(app, fg_color="transparent")
frameBotoes.grid(row=3, column=0, columnspan=5, pady=20)

btnCalcular = ctk.CTkButton(frameBotoes, text="CALCULAR EMISSÕES", 
                            font=("Arial", 22, "bold"), width=350, height=60,
                            fg_color="#1f6aa5", hover_color="#1557a0",
                            corner_radius=10,
                            command=lambda: set_resultado(get_valores()))
btnCalcular.pack(side="left", padx=15)

btnRelatorio = ctk.CTkButton(frameBotoes, text="VER RELATÓRIO COMPLETO", 
                             font=("Arial", 22, "bold"), width=350, height=60,
                             fg_color="#2d7a3e", hover_color="#256832",
                             corner_radius=10,
                             command=Srelatorio)
btnRelatorio.pack(side="left", padx=15)

btnCompensacao = ctk.CTkButton(frameBotoes, text="SISTEMA DE COMPENSAÇÃO", 
                               font=("Arial", 22, "bold"), width=350, height=60,
                               fg_color="#8b4513", hover_color="#6b3410",
                               corner_radius=10,
                               command=lambda: mostrar_compensacao(get_valores()))
btnCompensacao.pack(side="left", padx=15)
```

**Diferenciação Visual**:
- Azul para cálculo (ação primária)
- Verde para relatório (informação)
- Marrom para compensação (ação ambiental)
- Efeito hover reforça interatividade

### 4.4.6. Funções de Controle

**Coleta de Dados**:
```python
def get_valores():
    dados_tratados = tratar_dados({
        "eletricidade": entryEletro.get(),
        "combustivel": entryGasolina.get(),
        "voo": entryAviao.get(),
        "transporte": entryCarro.get(),
        "gas_natural": entryGas.get(),
        "agua": entryAgua.get(),
        "residuos": entryResiduos.get()
    })
    return dados_tratados
```

**Atualização de Resultado**:
```python
def set_resultado(dados):
    if dados:
        valor = calc_credito(dados)
        labelResultado.configure(text=f"{valor['total']:.2f} toneladas de CO2/ano")
    else:
        labelResultado.configure(text="Erro: Entrada inválida. Por favor, insira números válidos.")
```

## 4.5. Janela de Relatório Detalhado

### 4.5.1. Estrutura da Janela

```python
def Srelatorio():
    valores = get_valores()
    dados = calc_credito(valores)

    if valores is None:
        labelResultado.configure(text="Por favor, insira números válidos.")
        return

    relatorio = ctk.CTkToplevel(app)
    relatorio.title("Relatório Detalhado de Emissões")
    relatorio.geometry('1500x850')
    relatorio.grid_columnconfigure(0, weight=1)
```

**CTkToplevel**: Cria janela secundária que permanece acima da janela principal.

### 4.5.2. Exibição por Categoria

```python
categorias = [
    ("Eletricidade", dados.get('eletricidade', 0)),
    ("Combustível", dados.get('combustivel', 0)),
    ("Avião", dados.get('voo', 0)),
    ("Transporte Público", dados.get('Transporte', 0)),
    ("Gás Natural", dados.get('gas_natural', 0)),
    ("Água", dados.get('agua', 0)),
    ("Resíduos", dados.get('residuos', 0))
]

for nome, valor in categorias:
    if valor > 0:
        frameItem = ctk.CTkFrame(frameScroll, fg_color="#1a1a1a", corner_radius=10)
        frameItem.pack(fill="x", padx=20, pady=8)
        
        ctk.CTkLabel(frameItem, text=f"{nome}",
                     font=("Arial", 16, "bold"), text_color="white").pack(side="left", padx=20, pady=15)
        
        ctk.CTkLabel(frameItem, text=f"{valor:.2f} kg CO2/ano",
                     font=("Arial", 16, "bold"), text_color="#ff6b6b").pack(side="right", padx=20, pady=15)
```

**Funcionalidades**:
- Exibe apenas categorias com valores > 0
- Cards individuais para cada categoria
- Valores em vermelho (#ff6b6b) destacam impacto

### 4.5.3. Resumo de Compensação

```python
frameComp = ctk.CTkFrame(frameScroll, fg_color="#3a2a1a", corner_radius=15)
frameComp.pack(fill="x", padx=20, pady=20)

ctk.CTkLabel(frameComp, text="RESUMO DE COMPENSAÇÃO",
             font=("Arial", 22, "bold"), text_color="#ffd700").pack(pady=(20, 15))

infos = [
    (f"{dados['creditos']} créditos de carbono necessários"),
    (f"{dados['arvores']} árvores para plantar"),
    (f"R$ {dados['valor_compensacao']:.2f} valor estimado")
]

for info in infos:
    ctk.CTkLabel(frameComp, text=info,
                 font=("Arial", 16), text_color="white").pack(anchor="w", padx=40, pady=5)
```

## 4.6. Sistema de Compensação

### 4.6.1. Carregamento de Ações

```python
import json
import os

caminho_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'fatores.json')
caminho_json = os.path.abspath(caminho_json)

compensacoes = {}
try:
    with open(caminho_json, 'r', encoding='utf-8') as f:
        fatores = json.load(f)
        compensacoes = fatores.get('compensacao', {})
except FileNotFoundError:
    try:
        caminho_json = 'src/data/fatores.json'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            fatores = json.load(f)
            compensacoes = fatores.get('compensacao', {})
    except Exception as e:
        ctk.CTkLabel(frameScroll, text=f"Erro ao carregar dados de compensação: {str(e)}",
                     font=("Arial", 14), text_color="#ff6b6b").pack(pady=20)
```

**Tratamento Robusto**:
- Tenta caminho relativo primeiro
- Fallback para caminho alternativo
- Mensagem de erro clara se falhar

### 4.6.2. Cálculo de Quantidades

```python
if 'reducao_kg_ano' in comp:
    reducao_anual = comp['reducao_kg_ano']
    quantidade = int(total_emissao_kg / reducao_anual) + 1 if reducao_anual > 0 else 0
    unidade = "unidades"
    reducao_display = reducao_anual
elif 'reducao_kg_mes' in comp:
    reducao_mensal = comp['reducao_kg_mes']
    reducao_anual = reducao_mensal * 12
    quantidade = int(total_emissao_kg / reducao_anual) + 1 if reducao_anual > 0 else 0
    unidade = "unidades"
    reducao_display = reducao_anual
```

**Lógica**:
- Identifica se ação é anual ou mensal
- Converte mensal para anual (× 12)
- Calcula quantidade necessária para neutralizar emissões totais
- Adiciona 1 para garantir compensação completa

### 4.6.3. Exibição de Ações

```python
frameCard = ctk.CTkFrame(frameScroll, fg_color="#1a1a1a", corner_radius=10)
frameCard.pack(fill="x", padx=20, pady=10)

ctk.CTkLabel(frameCard, text=f"{comp['nome']}",
             font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", padx=20, pady=(15, 5))

if 'descricao' in comp:
    ctk.CTkLabel(frameCard, text=comp['descricao'],
                 font=("Arial", 12, "italic"), text_color="#b0b0b0").pack(anchor="w", padx=40, pady=2)

ctk.CTkLabel(frameCard, text=f"Compensa: {reducao_display:.2f} kg de CO2/ano por unidade",
             font=("Arial", 14), text_color="#90ee90").pack(anchor="w", padx=40, pady=5)

ctk.CTkLabel(frameCard, text=f"Quantidade necessária para neutralizar suas emissões: {quantidade} {unidade}",
             font=("Arial", 14, "bold"), text_color="#ffd700").pack(anchor="w", padx=40, pady=(2, 15))
```

**Hierarquia Visual**:
- Nome em destaque (20pt bold)
- Descrição em itálico (contexto)
- Valor de compensação em verde (positivo)
- Quantidade necessária em dourado (ação requerida)

---

## REFERÊNCIAS (Capítulo 4)

FOWLER, M. **Patterns of Enterprise Application Architecture**. Boston: Addison-Wesley, 2002.

GAMMA, E. et al. **Design Patterns: Elements of Reusable Object-Oriented Software**. Reading: Addison-Wesley, 1994.

NIELSEN, J.; BUDIU, R. **Mobile Usability**. Berkeley: New Riders, 2012.

NORMAN, D. A. **The Design of Everyday Things: Revised and Expanded Edition**. New York: Basic Books, 2013.

SHNEIDERMAN, B. et al. **Designing the User Interface: Strategies for Effective Human-Computer Interaction**. 6th ed. Boston: Pearson, 2016.
