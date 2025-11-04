# 📝 RESUMO DO PROJETO - GUIA RÁPIDO

## 🎯 O QUE É O PROJETO?

Calculadora Desktop de Emissões de CO² com sistema de compensação por créditos de carbono.

**Tecnologia:** Python + CustomTkinter (interface gráfica moderna)

---

## 📂 ARQUIVOS PRINCIPAIS

### 1. `src/main.py`
- **O que faz:** Inicia a aplicação
- **Código:** Apenas chama `start()` da view

### 2. `src/view/index.py`
- **O que faz:** Interface gráfica completa
- **Contém:**
  - 9 campos de entrada (eletricidade, gasolina, avião, etc.)
  - Botão "Calcular" - mostra total de CO²
  - Botão "Ver Relatório Completo" - abre janela detalhada
  - Janela de relatório com sistema de compensação

### 3. `src/utils/index.py`
- **O que faz:** Toda a lógica de cálculo
- **Funções principais:**
  - `tratar_dados()` - Valida entrada do usuário
  - `calc_credito()` - Calcula emissões e compensação
  - Funções individuais para cada fator (eletricidade, combustível, etc.)

### 4. `src/data/fatores.json`
- **O que faz:** Armazena fatores de emissão
- **Contém:** Valores de kg CO²/unidade para cada categoria

---

## 🔢 COMO FUNCIONA?

### Fluxo Básico:
```
1. Usuário preenche campos → 
2. Clica "Calcular" → 
3. Sistema valida dados → 
4. Calcula emissões (kg CO²) → 
5. Converte para toneladas → 
6. Exibe resultado
```

### Fórmula:
```
Total CO² = Σ (Consumo × Fator de Emissão)
```

### Sistema de Compensação:
```
Créditos = Total CO² em toneladas (arredondado para cima)
Árvores = Total CO² (kg) / 21.77
Valor R$ = Créditos × 50
```

---

## 📊 9 FATORES DE EMISSÃO

| Categoria | Unidade | Fator CO² |
|-----------|---------|-----------|
| Eletricidade | kWh/Mês | 0.038 kg/kWh |
| Gasolina | L/Dia | 2.348 kg/L |
| Avião | KM/Mês | 0.123 kg/km |
| Transporte Público | KM/Dia | 0.017 kg/km |
| Gás Natural | m³/Mês | 1.95 kg/m³ |
| Água | m³/Mês | 0.15 kg/m³ |
| Resíduos | kg/Mês | 0.5 kg/kg |
| Carne | kg/Semana | 27.0 kg/kg |
| Vegetariano | refeições/Semana | 0.5 kg/refeição |

---

## 🚀 COMO EXECUTAR

```bash
# 1. Instalar dependência
pip install customtkinter==5.2.2

# 2. Ir para pasta src
cd src

# 3. Executar
python main.py
```

---

## ✅ O QUE FOI IMPLEMENTADO

### ✅ Funcionalidades Básicas:
- [x] Cálculo de emissões (4 fatores originais)
- [x] Interface gráfica com CustomTkinter
- [x] Validação de entrada
- [x] Relatório básico

### ✅ Melhorias Implementadas:
- [x] **5 novos fatores de emissão** (gás, água, resíduos, alimentação)
- [x] **Sistema de compensação completo** (créditos, árvores, valor R$)
- [x] **Interface melhorada** (9 campos, layout organizado)
- [x] **Relatório detalhado** (exibe todas categorias + compensação)
- [x] **Validação aprimorada** (campos vazios = 0)

---

## 🎨 INTERFACE

### Tela Principal (1400x700):
```
┌─────────────────────────────────────────┐
│   Calculadora de Emissões de CO²       │
├─────────────────────────────────────────┤
│  [Eletricidade] [Gasolina] [Avião] [Transporte]  │
│  [Gás Natural]  [Água]     [Resíduos] [Carne]    │
│  [Vegetariano]                                    │
├─────────────────────────────────────────┤
│       TOTAL: X.XX toneladas CO²         │
├─────────────────────────────────────────┤
│   [Calcular] [Ver Relatório Completo]  │
└─────────────────────────────────────────┘
```

### Tela de Relatório (1400x700):
```
┌─────────────────────────────────────────┐
│     Extrato de Emissões de CO²         │
├─────────────────────────────────────────┤
│  Eletricidade: XX.XX kg CO²            │
│  Combustível: XX.XX kg CO²             │
│  ... (todas categorias)                │
├─────────────────────────────────────────┤
│  TOTAL: X.XX toneladas CO²             │
├─────────────────────────────────────────┤
│     SISTEMA DE COMPENSAÇÃO             │
│  • Créditos: X créditos                │
│  • Árvores: X árvores                  │
│  • Valor: R$ XX.XX                     │
└─────────────────────────────────────────┘
```

---

## 🐛 VALIDAÇÕES

### ✅ Aceita:
- Números positivos (inteiros ou decimais)
- Campos vazios (tratados como 0)
- Zero

### ❌ Rejeita:
- Números negativos
- Texto/letras
- Caracteres especiais

---

## 📚 DOCUMENTAÇÃO

- **README.md** - Visão geral e instruções
- **PRD.md** - Documento técnico completo (12 seções)
- **APS.md** - Requisitos originais do projeto APS
- **PROJETO_RESUMO.md** - Este arquivo (guia rápido)

---

## 🎓 NÍVEL DO PROJETO

**2º Semestre - Simples e Funcional**

### ✅ Mantido Simples:
- Sem banco de dados
- Sem histórico
- Sem gráficos complexos
- Sem login/usuários
- Sem APIs externas

### ✅ Foco em:
- Interface gráfica básica
- Cálculos matemáticos
- Validação de dados
- Estrutura de código limpa

---

## 🔧 ESTRUTURA DE CÓDIGO

```python
# main.py
from view.index import start
start()

# view/index.py
- get_valores() → Pega dados dos campos
- set_resultado() → Exibe resultado na tela
- Srelatorio() → Abre janela de relatório
- Interface completa (labels, entries, buttons)

# utils/index.py
- tratar_dados() → Valida entrada
- calc_credito() → Calcula tudo
- calc_eletricidade(), calc_combustivel(), etc.
- carregajson() → Lê fatores.json

# data/fatores.json
{ "eletricidade/kwh": 0.038, ... }
```

---

## 💡 DICAS PARA NÃO SE PERDER

1. **Sempre comece pelo `main.py`** - é o ponto de entrada
2. **A interface está em `view/index.py`** - tudo visual aqui
3. **Os cálculos estão em `utils/index.py`** - toda lógica aqui
4. **Os fatores estão em `fatores.json`** - valores de emissão
5. **Para testar:** Execute e preencha alguns campos com números

---

## 🎯 PRÓXIMOS PASSOS (SE QUISER EXPANDIR)

1. Adicionar mais fatores de emissão
2. Melhorar visual (cores, ícones)
3. Adicionar dicas/tooltips
4. Criar gráfico simples (pizza/barras)
5. Salvar último cálculo em arquivo

---

**Versão:** 1.0  
**Última Atualização:** Novembro 2024  
**Status:** ✅ Completo e Funcional
