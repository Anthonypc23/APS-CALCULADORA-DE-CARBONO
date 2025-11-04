# PRD - Calculadora de Carbono (APS 2º Semestre)

## 1. Visão Geral do Projeto

### 1.1 Objetivo
Aplicação desktop para calcular emissões de CO² baseadas em consumo diário/mensal do usuário e fornecer um sistema de compensação por créditos de carbono.

### 1.2 Tecnologias
- **Python 3.x**
- **CustomTkinter 5.2.2** - Interface gráfica moderna
- **JSON** - Armazenamento de fatores de emissão

### 1.3 Plataforma
- Desktop (Windows/Linux/Mac)

---

## 2. Arquitetura Atual

```
APS-CALCULADORA-DE-CARBONO/
├── src/
│   ├── main.py              # Entry point
│   ├── view/
│   │   ├── __init__.py
│   │   └── index.py         # Interface gráfica (CustomTkinter)
│   ├── utils/
│   │   ├── __init_.py
│   │   └── index.py         # Lógica de cálculo
│   └── data/
│       ├── __init__.py
│       └── fatores.json     # Fatores de emissão
├── requirements.txt
└── README.md
```

---

## 3. Funcionalidades Implementadas

### 3.1 Tela Principal
- **Inputs de Consumo:**
  - Eletricidade (kWh/Mês)
  - Gasolina (Litros/Dia)
  - Avião (KM/Mês)
  - Transporte Público (KM/Dia)

- **Botões:**
  - `Calcular` - Calcula total de CO² emitido
  - `Relatório` - Abre janela com detalhamento

### 3.2 Cálculo de Emissões
- **Fatores de Emissão (fatores.json):**
  - Eletricidade: 0.038 kg CO²/kWh
  - Combustível: 2.348 kg CO²/litro
  - Voo: 0.123 kg CO²/km
  - Transporte Público: 0.017 kg CO²/km

- **Fórmula:**
  ```
  Total CO² = (eletricidade × fator) + (combustível × fator) + 
              (voo × fator) + (transporte × fator)
  ```

### 3.3 Relatório
- Exibe detalhamento por categoria
- Mostra total de créditos (emissões totais)

---

## 4. Melhorias Implementadas

### 4.1 Novos Fatores de Emissão
Adicionados ao `fatores.json`:
- **Gás Natural** (m³/mês)
- **Consumo de Água** (m³/mês)
- **Resíduos/Lixo** (kg/mês)
- **Alimentação Carne** (kg/semana)
- **Alimentação Vegetariana** (refeições/semana)

### 4.2 Sistema de Compensação de Créditos
Implementado na tela de Relatório:
- **Cálculo de Créditos Necessários:**
  - 1 crédito = 1 tonelada de CO²
  - Exibe quantos créditos são necessários para neutralizar

- **Sugestões de Compensação:**
  - Plantio de árvores (quantidade estimada)
  - Projetos de energia renovável
  - Valor estimado em R$ para compensação

### 4.3 Melhorias na Interface
- Validação de entrada aprimorada
- Mensagens de erro mais claras
- Layout responsivo melhorado
- Cores e espaçamento otimizados

---

## 5. Fluxo de Uso

```
1. Usuário abre aplicação
   ↓
2. Preenche campos de consumo
   ↓
3. Clica em "Calcular"
   ↓
4. Sistema valida dados (números positivos)
   ↓
5. Exibe total de CO² na tela principal
   ↓
6. Usuário clica em "Relatório"
   ↓
7. Abre janela com:
   - Detalhamento por categoria
   - Total de emissões
   - Créditos necessários
   - Sugestões de compensação
```

---

## 6. Estrutura de Dados

### 6.1 Entrada do Usuário
```python
{
    "eletricidade": float,      # kWh/mês
    "combustivel": float,       # litros/dia
    "voo": float,              # km/mês
    "transporte": float,       # km/dia
    "gas_natural": float,      # m³/mês
    "agua": float,             # m³/mês
    "residuos": float,         # kg/mês
    "carne": float,            # kg/semana
    "vegetariano": float       # refeições/semana
}
```

### 6.2 Resultado do Cálculo
```python
{
    "eletricidade": float,     # kg CO²
    "combustivel": float,      # kg CO²
    "voo": float,             # kg CO²
    "Transporte": float,      # kg CO²
    "gas_natural": float,     # kg CO²
    "agua": float,            # kg CO²
    "residuos": float,        # kg CO²
    "alimentacao": float,     # kg CO²
    "total": float,           # toneladas CO²
    "creditos": int,          # créditos necessários
    "arvores": int,           # árvores para plantar
    "valor_compensacao": float # R$ estimado
}
```

---

## 7. Fórmulas de Compensação

### 7.1 Créditos de Carbono
```
Créditos = Total CO² (toneladas) arredondado para cima
```

### 7.2 Plantio de Árvores
```
Árvores = Total CO² (kg) / 21.77
# Uma árvore absorve ~21.77 kg CO²/ano
```

### 7.3 Valor de Compensação
```
Valor (R$) = Créditos × 50
# Preço médio simplificado de R$ 50/crédito
```

---

## 8. Validações

### 8.1 Entrada de Dados
- ✅ Aceita apenas números
- ✅ Valores devem ser ≥ 0
- ✅ Campos vazios = 0
- ❌ Valores negativos
- ❌ Texto/caracteres especiais

### 8.2 Tratamento de Erros
- Mensagem clara ao usuário
- Não permite cálculo com dados inválidos
- Mantém dados válidos anteriores

---

## 9. Limitações (Escopo 2º Semestre)

### O que NÃO foi implementado:
- ❌ Banco de dados persistente
- ❌ Histórico de cálculos
- ❌ Gráficos/visualizações
- ❌ Exportação de relatórios (PDF/Excel)
- ❌ Sistema de login/usuários
- ❌ Integração com APIs externas
- ❌ Cálculos avançados (Escopo 1, 2, 3)

### Justificativa:
Projeto focado em conceitos básicos de:
- Interface gráfica com CustomTkinter
- Manipulação de arquivos JSON
- Cálculos matemáticos simples
- Estrutura de projeto Python

---

## 10. Como Executar

### 10.1 Instalação
```bash
# Instalar dependências
pip install -r requirements.txt
```

### 10.2 Execução
```bash
# Navegar até a pasta src
cd src

# Executar aplicação
python main.py
```

---

## 11. Possíveis Expansões Futuras

### Para semestres avançados:
1. **Persistência de Dados**
   - SQLite para histórico
   - Comparação mensal/anual

2. **Visualizações**
   - Gráficos de pizza/barras
   - Evolução temporal

3. **Gamificação**
   - Metas de redução
   - Badges/conquistas

4. **Marketplace de Créditos**
   - Integração com projetos reais
   - Sistema de compra/venda

5. **Relatórios Avançados**
   - Exportação PDF
   - Comparação com médias nacionais

---

## 12. Referências

### Fatores de Emissão:
- IPCC (Intergovernmental Panel on Climate Change)
- GHG Protocol Brasil
- Ministério do Meio Ambiente

### Compensação:
- Valores médios de mercado de créditos de carbono
- Estimativas de absorção por árvores nativas brasileiras

---

**Versão:** 1.0  
**Data:** Novembro 2024  
**Nível:** 2º Semestre - Projeto APS
