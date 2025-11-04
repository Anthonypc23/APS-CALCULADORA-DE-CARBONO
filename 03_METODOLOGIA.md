# 3. METODOLOGIA

## 3.1. Tipo de Pesquisa

Este trabalho caracteriza-se como uma pesquisa aplicada de natureza tecnológica, com abordagem quali-quantitativa. Segundo Gil (2017), pesquisas aplicadas têm como objetivo gerar conhecimentos para aplicação prática dirigida à solução de problemas específicos. No contexto deste projeto, o problema específico é a necessidade de uma ferramenta acessível para cálculo e monitoramento de pegada de carbono individual.

### 3.1.1. Classificação Metodológica

**Quanto à Natureza**: Pesquisa aplicada, pois visa desenvolver uma solução prática para um problema real (PRODANOV; FREITAS, 2013).

**Quanto aos Objetivos**: Pesquisa exploratória e descritiva. Exploratória por investigar ferramentas existentes e identificar lacunas; descritiva por documentar o processo de desenvolvimento e as características do sistema implementado (GIL, 2017).

**Quanto à Abordagem**: Quali-quantitativa, combinando análise qualitativa de requisitos e funcionalidades com análise quantitativa de dados de emissões e validação de cálculos (CRESWELL; CLARK, 2017).

**Quanto aos Procedimentos**: Pesquisa bibliográfica, documental e experimental. Bibliográfica pela revisão de literatura científica; documental pela análise de relatórios técnicos e normas; experimental pelo desenvolvimento e teste do sistema (LAKATOS; MARCONI, 2017).

### 3.1.2. Etapas da Pesquisa

O desenvolvimento deste trabalho seguiu as seguintes etapas:

1. **Revisão Bibliográfica**: Estudo de literatura científica sobre mudanças climáticas, pegada de carbono, fatores de emissão e metodologias de cálculo.

2. **Análise de Requisitos**: Identificação de necessidades dos usuários e definição de requisitos funcionais e não-funcionais do sistema.

3. **Coleta de Dados**: Levantamento de fatores de emissão de fontes confiáveis (IPCC, GHG Protocol, MCTI).

4. **Desenvolvimento do Sistema**: Implementação da aplicação seguindo metodologia ágil iterativa.

5. **Testes e Validação**: Verificação da precisão dos cálculos e usabilidade da interface.

6. **Documentação**: Elaboração de documentação técnica e acadêmica do projeto.

## 3.2. Coleta de Dados

### 3.2.1. Fontes de Dados

Os dados utilizados neste projeto foram coletados de fontes primárias reconhecidas internacionalmente:

**IPCC (Intergovernmental Panel on Climate Change)**: Forneceu fatores de emissão padrão para combustíveis fósseis, gás natural e resíduos. As diretrizes do IPCC de 2006 para inventários nacionais de gases de efeito estufa são a referência global para metodologias de cálculo (IPCC, 2006).

**GHG Protocol**: Protocolo desenvolvido pelo World Resources Institute (WRI) e World Business Council for Sustainable Development (WBCSD), fornecendo padrões para contabilização corporativa de emissões (WRI; WBCSD, 2004).

**Ministério da Ciência, Tecnologia e Inovação (MCTI)**: Fonte dos fatores de emissão específicos para o Sistema Interligado Nacional (SIN) brasileiro, atualizados anualmente considerando a composição da matriz energética nacional (MCTI, 2023).

**DEFRA (Department for Environment, Food and Rural Affairs - UK)**: Forneceu fatores de emissão para transporte aéreo, considerando efeitos de altitude e diferentes classes de voo (DEFRA, 2023).

**Estudos Científicos Revisados por Pares**: Dados sobre emissões de alimentos foram obtidos de Poore e Nemecek (2018), meta-análise de 38.700 fazendas em 119 países, publicada na revista Science.

### 3.2.2. Critérios de Seleção de Dados

Os fatores de emissão foram selecionados com base nos seguintes critérios:

1. **Confiabilidade da Fonte**: Priorização de dados de organizações internacionais reconhecidas e estudos revisados por pares.

2. **Atualidade**: Utilização de dados mais recentes disponíveis (2020-2023).

3. **Relevância Geográfica**: Quando disponível, preferência por fatores específicos para o contexto brasileiro.

4. **Completude**: Seleção de fatores que cobrem as principais fontes de emissões individuais.

5. **Consistência Metodológica**: Garantia de que diferentes fatores utilizam metodologias compatíveis.

### 3.2.3. Tratamento e Validação de Dados

Os dados coletados passaram por processo de validação:

**Verificação Cruzada**: Comparação de valores de múltiplas fontes para identificar discrepâncias.

**Análise de Incertezas**: Documentação de margens de erro e incertezas associadas aos fatores.

**Conversão de Unidades**: Padronização de todas as medidas para unidades consistentes (kg CO₂/unidade).

**Documentação**: Registro detalhado de todas as fontes e metodologias utilizadas para cada fator.

## 3.3. Ferramentas e Tecnologias

### 3.3.1. Linguagem de Programação

**Python 3.11**: Escolhida como linguagem principal do projeto pelos seguintes motivos:

- **Facilidade de Aprendizado**: Sintaxe clara e legível, facilitando manutenção e evolução do código (VAN ROSSUM; DRAKE, 2009).

- **Bibliotecas Robustas**: Ecossistema rico de bibliotecas para desenvolvimento de interfaces gráficas, manipulação de dados e cálculos científicos.

- **Portabilidade**: Código Python pode ser executado em diferentes sistemas operacionais (Windows, macOS, Linux) com mínimas modificações.

- **Comunidade Ativa**: Grande comunidade de desenvolvedores, facilitando resolução de problemas e acesso a recursos educacionais.

- **Adequação Acadêmica**: Amplamente utilizada em contextos educacionais e pesquisa científica.

### 3.3.2. Biblioteca de Interface Gráfica

**CustomTkinter 5.2.2**: Biblioteca moderna para criação de interfaces gráficas, escolhida por:

- **Design Moderno**: Oferece widgets com aparência contemporânea, superando limitações visuais do Tkinter padrão (AKASCAPE, 2023).

- **Facilidade de Uso**: API similar ao Tkinter, reduzindo curva de aprendizado.

- **Temas Personalizáveis**: Suporte nativo para modo escuro e personalização de cores.

- **Performance**: Boa performance mesmo em computadores com recursos limitados.

- **Documentação**: Documentação clara e exemplos práticos disponíveis.

**Alternativas Consideradas**:
- **PyQt5**: Mais poderosa, mas com curva de aprendizado mais íngreme e licenciamento complexo.
- **Kivy**: Focada em aplicações móveis, menos adequada para desktop.
- **Tkinter Padrão**: Interface visual datada, menos atraente para usuários.

### 3.3.3. Formato de Armazenamento de Dados

**JSON (JavaScript Object Notation)**: Utilizado para armazenar fatores de emissão e configurações:

- **Legibilidade**: Formato texto facilmente legível por humanos e máquinas.
- **Estrutura Hierárquica**: Permite organização lógica de dados relacionados.
- **Suporte Nativo**: Python possui biblioteca json integrada.
- **Facilidade de Atualização**: Fatores podem ser atualizados editando arquivo de texto.
- **Portabilidade**: Formato independente de plataforma.

### 3.3.4. Ambiente de Desenvolvimento

**Visual Studio Code**: Editor de código utilizado, oferecendo:
- Syntax highlighting para Python
- Integração com Git para controle de versão
- Extensões para Python (Pylance, Python Debugger)
- Terminal integrado

**Git/GitHub**: Sistema de controle de versão para:
- Rastreamento de mudanças no código
- Colaboração (se aplicável)
- Backup e histórico de desenvolvimento

### 3.3.5. Ferramentas de Teste e Validação

**Python unittest**: Framework de testes unitários integrado ao Python.

**Calculadoras de Referência**: Comparação de resultados com:
- Carbon Footprint Calculator (carbonfootprint.com)
- EPA Carbon Footprint Calculator
- WWF Footprint Calculator

## 3.4. Desenvolvimento do Sistema

### 3.4.1. Metodologia de Desenvolvimento

O projeto seguiu princípios de **desenvolvimento ágil iterativo**, adaptado para contexto acadêmico individual:

**Sprints Semanais**: Desenvolvimento organizado em ciclos semanais, cada um focado em conjunto específico de funcionalidades.

**Iteração Contínua**: Refinamento constante baseado em testes e feedback.

**Documentação Paralela**: Documentação desenvolvida simultaneamente ao código, não como etapa posterior.

**Prototipagem Rápida**: Desenvolvimento de protótipos funcionais para validação de conceitos antes de implementação completa.

### 3.4.2. Arquitetura do Sistema

O sistema foi desenvolvido seguindo padrão arquitetural **MVC (Model-View-Controller)** adaptado:

**Model (Modelo)**: 
- Arquivo `fatores.json`: Armazena dados de fatores de emissão
- Módulo `utils/index.py`: Contém lógica de negócio e cálculos

**View (Visão)**:
- Módulo `view/index.py`: Implementa interface gráfica e interação com usuário

**Controller (Controlador)**:
- Funções de tratamento de dados e validação
- Gerenciamento de fluxo entre interface e cálculos

**Justificativa da Arquitetura**: Separação de responsabilidades facilita manutenção, testes e possíveis extensões futuras (GAMMA et al., 1994).

### 3.4.3. Estrutura de Diretórios

```
APS-CALCULADORA-DE-CARBONO/
│
├── src/
│   ├── main.py                 # Ponto de entrada da aplicação
│   ├── view/
│   │   └── index.py           # Interface gráfica
│   ├── utils/
│   │   └── index.py           # Funções de cálculo
│   └── data/
│       └── fatores.json       # Fatores de emissão
│
├── docs/
│   ├── PRD.md                 # Product Requirements Document
│   ├── PROJETO_RESUMO.md      # Resumo do projeto
│   └── MELHORIAS_VISUAIS.md   # Documentação de design
│
├── README.md                   # Documentação principal
├── requirements.txt            # Dependências do projeto
└── APS.md                     # Requisitos acadêmicos
```

### 3.4.4. Processo de Implementação

**Fase 1 - Configuração Inicial (Semana 1)**:
- Configuração do ambiente de desenvolvimento
- Instalação de dependências
- Criação da estrutura de diretórios
- Implementação do arquivo de entrada (main.py)

**Fase 2 - Módulo de Cálculos (Semana 2)**:
- Implementação de funções de cálculo para cada categoria
- Desenvolvimento da função de agregação de emissões
- Criação do sistema de tratamento e validação de dados
- Testes unitários dos cálculos

**Fase 3 - Interface Gráfica Básica (Semana 3)**:
- Desenvolvimento da janela principal
- Implementação de campos de entrada
- Criação de botões de ação
- Exibição de resultados básicos

**Fase 4 - Sistema de Relatórios (Semana 4)**:
- Desenvolvimento da janela de relatório detalhado
- Implementação de visualização por categoria
- Cálculo de créditos de carbono
- Estimativa de árvores necessárias

**Fase 5 - Sistema de Compensação (Semana 5)**:
- Pesquisa e documentação de ações de compensação
- Implementação da janela de compensação
- Cálculo de quantidades necessárias
- Interface visual para ações

**Fase 6 - Refinamento Visual (Semana 6)**:
- Aplicação de paleta de cores consistente
- Melhoria de layout e espaçamento
- Implementação de feedback visual
- Testes de usabilidade

**Fase 7 - Ajustes e Otimização (Semana 7)**:
- Correção de bugs identificados
- Otimização de performance
- Ajuste de cálculos para valores anuais
- Refinamento de interface

**Fase 8 - Documentação e Testes Finais (Semana 8)**:
- Elaboração de documentação técnica
- Testes de integração
- Validação de cálculos
- Preparação de material de apresentação

### 3.4.5. Padrões de Codificação

O código seguiu convenções estabelecidas pela comunidade Python:

**PEP 8**: Guia de estilo oficial para código Python, incluindo:
- Indentação de 4 espaços
- Linhas com máximo de 79 caracteres (flexibilizado para 100 em alguns casos)
- Nomenclatura snake_case para funções e variáveis
- Nomenclatura PascalCase para classes

**Comentários e Docstrings**: Documentação inline para funções complexas e módulos.

**Modularização**: Funções pequenas e focadas, cada uma com responsabilidade única.

**Tratamento de Erros**: Uso de try-except para operações que podem falhar (leitura de arquivos, conversão de tipos).

### 3.4.6. Controle de Qualidade

**Testes Manuais**: Verificação manual de funcionalidades após cada implementação.

**Testes de Cálculo**: Comparação de resultados com valores conhecidos e calculadoras de referência.

**Testes de Interface**: Verificação de responsividade e comportamento em diferentes resoluções.

**Validação de Dados**: Testes com entradas válidas, inválidas e casos extremos.

**Code Review**: Revisão periódica do código para identificar possíveis melhorias.

## 3.5. Validação e Testes

### 3.5.1. Validação de Cálculos

A precisão dos cálculos foi validada através de múltiplas abordagens:

**Comparação com Calculadoras Estabelecidas**: Resultados foram comparados com:
- Carbon Footprint Calculator (carbonfootprint.com)
- EPA Carbon Footprint Calculator
- Calculadora do Programa Brasileiro GHG Protocol

**Casos de Teste Conhecidos**: Utilização de cenários com resultados esperados documentados na literatura.

**Verificação de Unidades**: Confirmação de que todas as conversões de unidades estão corretas.

**Análise de Sensibilidade**: Verificação de que mudanças nos inputs produzem mudanças proporcionais e esperadas nos outputs.

### 3.5.2. Testes de Usabilidade

Embora não tenha sido realizado teste formal com usuários, a interface foi avaliada considerando:

**Princípios de Nielsen**: Heurísticas de usabilidade de Jakob Nielsen (NIELSEN, 1994):
- Visibilidade do status do sistema
- Correspondência entre sistema e mundo real
- Controle e liberdade do usuário
- Consistência e padrões
- Prevenção de erros
- Reconhecimento ao invés de memorização
- Flexibilidade e eficiência de uso
- Design estético e minimalista
- Ajuda aos usuários no reconhecimento, diagnóstico e recuperação de erros
- Ajuda e documentação

**Acessibilidade**: Considerações sobre:
- Contraste de cores adequado
- Tamanhos de fonte legíveis
- Organização lógica de elementos
- Feedback claro de ações

### 3.5.3. Testes de Robustez

**Entradas Inválidas**: Verificação de comportamento com:
- Valores negativos
- Valores não numéricos
- Campos vazios
- Valores extremamente grandes

**Casos Extremos**: Teste com:
- Todos os campos zerados
- Todos os campos com valores máximos
- Combinações incomuns de valores

**Tratamento de Erros**: Verificação de que erros são capturados e mensagens apropriadas são exibidas.

## 3.6. Limitações Metodológicas

### 3.6.1. Limitações Reconhecidas

**Escopo de Emissões**: O sistema calcula apenas emissões diretas e algumas indiretas (Escopo 1 e 2, parcialmente Escopo 3). Não inclui:
- Emissões incorporadas em produtos manufaturados
- Emissões de serviços financeiros
- Emissões de infraestrutura pública

**Fatores de Emissão Médios**: Utilização de valores médios pode não refletir situações específicas:
- Eficiência real de veículos varia
- Matriz energética varia regionalmente
- Práticas agrícolas afetam emissões de alimentos

**Ausência de Análise de Ciclo de Vida Completa**: Cálculos focam em fase de uso, não considerando:
- Emissões de fabricação de equipamentos
- Emissões de construção de infraestrutura
- Emissões de descarte e reciclagem

**Validação Limitada**: Ausência de testes com usuários reais e validação estatística robusta.

### 3.6.2. Mitigação de Limitações

**Transparência**: Documentação clara de metodologias e fontes de dados.

**Conservadorismo**: Quando múltiplos valores estavam disponíveis, preferência por estimativas conservadoras.

**Documentação de Incertezas**: Reconhecimento explícito de margens de erro.

**Extensibilidade**: Arquitetura permite fácil atualização de fatores e adição de novas categorias.

---

## REFERÊNCIAS (Capítulo 3)

AKASCAPE. **CustomTkinter Documentation**. GitHub, 2023. Disponível em: https://github.com/TomSchimansky/CustomTkinter. Acesso em: 15 out. 2024.

CRESWELL, J. W.; CLARK, V. L. P. **Designing and conducting mixed methods research**. 3rd ed. Thousand Oaks: SAGE Publications, 2017.

DEFRA. **Greenhouse gas reporting: conversion factors 2023**. London: Department for Environment, Food and Rural Affairs, 2023.

GAMMA, E. et al. **Design patterns: elements of reusable object-oriented software**. Reading: Addison-Wesley, 1994.

GIL, A. C. **Como elaborar projetos de pesquisa**. 6. ed. São Paulo: Atlas, 2017.

IPCC. **2006 IPCC Guidelines for National Greenhouse Gas Inventories**. Hayama: Institute for Global Environmental Strategies, 2006.

LAKATOS, E. M.; MARCONI, M. A. **Fundamentos de metodologia científica**. 8. ed. São Paulo: Atlas, 2017.

MCTI. **Fator médio de emissão de CO₂ do Sistema Interligado Nacional do Brasil**. Brasília: Ministério da Ciência, Tecnologia e Inovação, 2023.

NIELSEN, J. **Usability engineering**. San Francisco: Morgan Kaufmann, 1994.

POORE, J.; NEMECEK, T. Reducing food's environmental impacts through producers and consumers. **Science**, v. 360, n. 6392, p. 987-992, 2018.

PRODANOV, C. C.; FREITAS, E. C. **Metodologia do trabalho científico: métodos e técnicas da pesquisa e do trabalho acadêmico**. 2. ed. Novo Hamburgo: Feevale, 2013.

VAN ROSSUM, G.; DRAKE, F. L. **The Python language reference manual**. Bristol: Network Theory, 2009.

WRI; WBCSD. **The Greenhouse Gas Protocol: A Corporate Accounting and Reporting Standard**. Washington, DC: World Resources Institute and World Business Council for Sustainable Development, 2004.
