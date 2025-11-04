# CALCULADORA DE PEGADA DE CARBONO
## Sistema de Monitoramento e Compensação de Emissões de CO₂

---

**Atividade Prática Supervisionada (APS)**  
**Curso:** Ciência da Computação  
**Semestre:** 2º Semestre  
**Ano:** 2024  

---

**Autores:**  
[Nome do Aluno]  
RA: [Número do RA]  

**Orientador:**  
[Nome do Professor]  

**Instituição:**  
[Nome da Universidade]  
[Campus]  

---

**Data:** Novembro de 2024

---

<div style="page-break-after: always;"></div>

# RESUMO

Este trabalho apresenta o desenvolvimento de uma aplicação desktop para cálculo e monitoramento de emissões de dióxido de carbono (CO₂) baseada em dados de consumo individual. O sistema, desenvolvido em Python utilizando a biblioteca CustomTkinter, permite que usuários calculem sua pegada de carbono anual considerando sete fatores principais: consumo de eletricidade, combustível veicular, viagens aéreas, transporte público, gás natural, água e geração de resíduos. A aplicação não apenas quantifica as emissões, mas também oferece um sistema inovador de compensação ambiental, apresentando oito ações práticas que podem ser adotadas para neutralizar o impacto ambiental individual. Os cálculos são baseados em fatores de emissão reconhecidos internacionalmente pelo IPCC (Intergovernmental Panel on Climate Change) e pelo GHG Protocol Brasil. O sistema gera relatórios detalhados, calcula créditos de carbono necessários para compensação e estima o número de árvores que precisariam ser plantadas para neutralizar as emissões. A interface gráfica moderna e intuitiva facilita o uso por pessoas sem conhecimento técnico, democratizando o acesso à informação sobre impacto ambiental pessoal. Os resultados demonstram que a ferramenta é eficaz para conscientização ambiental e pode servir como base para tomada de decisões sustentáveis no cotidiano.

**Palavras-chave:** Pegada de Carbono, Emissões de CO₂, Sustentabilidade, Python, Compensação Ambiental, Créditos de Carbono.

---

<div style="page-break-after: always;"></div>

# ABSTRACT

This work presents the development of a desktop application for calculating and monitoring carbon dioxide (CO₂) emissions based on individual consumption data. The system, developed in Python using the CustomTkinter library, allows users to calculate their annual carbon footprint considering seven main factors: electricity consumption, vehicle fuel, air travel, public transportation, natural gas, water, and waste generation. The application not only quantifies emissions but also offers an innovative environmental compensation system, presenting eight practical actions that can be adopted to neutralize individual environmental impact. Calculations are based on emission factors internationally recognized by the IPCC (Intergovernmental Panel on Climate Change) and GHG Protocol Brazil. The system generates detailed reports, calculates carbon credits needed for compensation, and estimates the number of trees that would need to be planted to neutralize emissions. The modern and intuitive graphical interface facilitates use by people without technical knowledge, democratizing access to information about personal environmental impact. Results demonstrate that the tool is effective for environmental awareness and can serve as a basis for sustainable decision-making in daily life.

**Keywords:** Carbon Footprint, CO₂ Emissions, Sustainability, Python, Environmental Compensation, Carbon Credits.

---

<div style="page-break-after: always;"></div>

# LISTA DE FIGURAS

Figura 1 - Tela Principal da Aplicação  
Figura 2 - Interface de Entrada de Dados  
Figura 3 - Relatório Detalhado de Emissões  
Figura 4 - Sistema de Compensação de Carbono  
Figura 5 - Arquitetura do Sistema  
Figura 6 - Fluxo de Dados da Aplicação  
Figura 7 - Estrutura de Diretórios do Projeto  
Figura 8 - Diagrama de Classes  

---

# LISTA DE TABELAS

Tabela 1 - Fatores de Emissão Utilizados  
Tabela 2 - Ações de Compensação e Seus Valores  
Tabela 3 - Comparação de Emissões por Categoria  
Tabela 4 - Tecnologias Utilizadas no Desenvolvimento  
Tabela 5 - Requisitos Funcionais do Sistema  
Tabela 6 - Requisitos Não-Funcionais do Sistema  
Tabela 7 - Casos de Teste Realizados  

---

# LISTA DE ABREVIATURAS E SIGLAS

**APS** - Atividades Práticas Supervisionadas  
**CO₂** - Dióxido de Carbono  
**GEE** - Gases de Efeito Estufa  
**IPCC** - Intergovernmental Panel on Climate Change (Painel Intergovernamental sobre Mudanças Climáticas)  
**GHG** - Greenhouse Gas (Gás de Efeito Estufa)  
**kWh** - Quilowatt-hora  
**GUI** - Graphical User Interface (Interface Gráfica do Usuário)  
**JSON** - JavaScript Object Notation  
**MVC** - Model-View-Controller  
**ONU** - Organização das Nações Unidas  
**UNFCCC** - United Nations Framework Convention on Climate Change  
**tCO₂e** - Toneladas de CO₂ equivalente  

---

<div style="page-break-after: always;"></div>

# SUMÁRIO

1. INTRODUÇÃO
   1.1. Contextualização
   1.2. Justificativa
   1.3. Objetivos
      1.3.1. Objetivo Geral
      1.3.2. Objetivos Específicos
   1.4. Estrutura do Trabalho

2. FUNDAMENTAÇÃO TEÓRICA
   2.1. Mudanças Climáticas e Aquecimento Global
   2.2. Pegada de Carbono
   2.3. Fatores de Emissão
   2.4. Créditos de Carbono
   2.5. Compensação Ambiental

3. METODOLOGIA
   3.1. Tipo de Pesquisa
   3.2. Coleta de Dados
   3.3. Ferramentas e Tecnologias
   3.4. Desenvolvimento do Sistema

4. DESENVOLVIMENTO DO SISTEMA
   4.1. Arquitetura
   4.2. Modelagem de Dados
   4.3. Interface Gráfica
   4.4. Módulos de Cálculo
   4.5. Sistema de Compensação

5. RESULTADOS E DISCUSSÃO
   5.1. Funcionalidades Implementadas
   5.2. Testes Realizados
   5.3. Análise de Resultados

6. CONSIDERAÇÕES FINAIS
   6.1. Conclusões
   6.2. Trabalhos Futuros

7. REFERÊNCIAS BIBLIOGRÁFICAS

8. ANEXOS

---

<div style="page-break-after: always;"></div>

# 1. INTRODUÇÃO

## 1.1. Contextualização

As mudanças climáticas representam um dos maiores desafios enfrentados pela humanidade no século XXI. Segundo o Sexto Relatório de Avaliação do IPCC (2021), as atividades humanas inequivocamente causaram o aquecimento global, com a temperatura da superfície terrestre aumentando aproximadamente 1,1°C desde o período pré-industrial (1850-1900). Este aquecimento é principalmente atribuído às emissões de gases de efeito estufa (GEE), sendo o dióxido de carbono (CO₂) o principal contribuinte, representando cerca de 76% das emissões globais de GEE (IPCC, 2021).

O conceito de "pegada de carbono" emergiu como uma ferramenta essencial para quantificar o impacto ambiental de indivíduos, organizações e produtos. Definida como a quantidade total de emissões de GEE causadas direta ou indiretamente por uma entidade, a pegada de carbono tornou-se um indicador crucial para a tomada de decisões sustentáveis (WIEDMANN; MINX, 2008). A conscientização sobre a pegada de carbono individual é fundamental para promover mudanças comportamentais que contribuam para a mitigação das mudanças climáticas.

No Brasil, o setor energético é responsável por aproximadamente 19% das emissões de GEE, seguido pelo setor de transportes com 12%, segundo o Sistema de Estimativas de Emissões de Gases de Efeito Estufa (SEEG) do Observatório do Clima (2023). Estes dados evidenciam a importância de ferramentas que permitam aos cidadãos compreender e monitorar suas contribuições individuais para as emissões nacionais.

A tecnologia da informação desempenha um papel fundamental na democratização do acesso à informação ambiental. Aplicações computacionais podem processar dados complexos e apresentá-los de forma acessível, permitindo que indivíduos sem formação técnica compreendam seu impacto ambiental e tomem decisões informadas. Neste contexto, o desenvolvimento de uma calculadora de pegada de carbono representa uma contribuição significativa para a educação ambiental e a promoção de práticas sustentáveis.

## 1.2. Justificativa

A necessidade de ferramentas práticas e acessíveis para cálculo de emissões de carbono é amplamente reconhecida na literatura científica. Pandey et al. (2011) argumentam que calculadoras de carbono são instrumentos eficazes para aumentar a conscientização pública sobre questões climáticas e promover mudanças comportamentais. Entretanto, muitas ferramentas disponíveis apresentam limitações significativas:

1. **Complexidade de Uso**: Muitas calculadoras existentes requerem conhecimento técnico especializado ou dados difíceis de obter, limitando sua adoção pelo público geral (PADGETT et al., 2008).

2. **Falta de Contextualização**: Ferramentas que apenas apresentam números sem oferecer soluções práticas para compensação falham em motivar ações concretas (WRIGHT; KEMP; WILLIAMS, 2011).

3. **Ausência de Localização**: Calculadoras internacionais frequentemente não consideram fatores de emissão específicos do contexto brasileiro, resultando em estimativas imprecisas (ROSA; SANTOS, 2019).

4. **Dependência de Plataformas Online**: Muitas soluções requerem conexão constante com a internet, limitando o acesso em regiões com conectividade precária.

Este projeto justifica-se pela necessidade de desenvolver uma ferramenta que supere estas limitações, oferecendo:

- **Interface Intuitiva**: Design focado na experiência do usuário, permitindo uso por pessoas sem conhecimento técnico.
- **Sistema de Compensação Integrado**: Não apenas calcula emissões, mas oferece soluções práticas e quantificadas para neutralização.
- **Adaptação ao Contexto Brasileiro**: Utiliza fatores de emissão específicos para a realidade nacional.
- **Funcionamento Offline**: Aplicação desktop que não depende de conexão com a internet.
- **Código Aberto**: Permite auditoria, adaptação e evolução contínua pela comunidade.

Além disso, o projeto alinha-se com os Objetivos de Desenvolvimento Sustentável (ODS) da ONU, especificamente:
- **ODS 13**: Ação contra a mudança global do clima
- **ODS 12**: Consumo e produção responsáveis
- **ODS 4**: Educação de qualidade (através da conscientização ambiental)

## 1.3. Objetivos

### 1.3.1. Objetivo Geral

Desenvolver uma aplicação desktop para cálculo de pegada de carbono individual, com sistema integrado de compensação ambiental, que seja acessível, precisa e educativa, contribuindo para a conscientização e adoção de práticas sustentáveis.

### 1.3.2. Objetivos Específicos

1. **Implementar módulo de cálculo de emissões** baseado em fatores reconhecidos internacionalmente, considerando sete categorias principais de consumo (eletricidade, combustível, transporte aéreo, transporte público, gás natural, água e resíduos).

2. **Desenvolver interface gráfica intuitiva** utilizando princípios de design centrado no usuário, garantindo acessibilidade e facilidade de uso.

3. **Criar sistema de compensação ambiental** que apresente ações práticas quantificadas para neutralização de emissões, incluindo plantio de árvores, uso de transporte sustentável, reciclagem e outras práticas.

4. **Gerar relatórios detalhados** que apresentem a distribuição de emissões por categoria, facilitando a identificação de áreas prioritárias para redução.

5. **Calcular equivalências práticas** como número de árvores necessárias para compensação e valor estimado em créditos de carbono.

6. **Validar a precisão dos cálculos** através de comparação com dados de referência e ferramentas estabelecidas.

7. **Documentar completamente o sistema** incluindo código-fonte, metodologia de cálculo e guias de uso.

8. **Garantir escalabilidade e manutenibilidade** através de arquitetura modular e boas práticas de programação.

## 1.4. Estrutura do Trabalho

Este trabalho está organizado em oito capítulos principais:

O **Capítulo 1 (Introdução)** apresenta o contexto das mudanças climáticas, justifica a necessidade da ferramenta desenvolvida e estabelece os objetivos do projeto.

O **Capítulo 2 (Fundamentação Teórica)** revisa a literatura científica sobre mudanças climáticas, pegada de carbono, fatores de emissão e sistemas de compensação ambiental, estabelecendo a base conceitual do trabalho.

O **Capítulo 3 (Metodologia)** descreve os métodos de pesquisa utilizados, as ferramentas e tecnologias empregadas, e o processo de desenvolvimento do sistema.

O **Capítulo 4 (Desenvolvimento do Sistema)** detalha a arquitetura da aplicação, a modelagem de dados, a implementação da interface gráfica e dos módulos de cálculo.

O **Capítulo 5 (Resultados e Discussão)** apresenta as funcionalidades implementadas, os testes realizados e analisa os resultados obtidos.

O **Capítulo 6 (Considerações Finais)** sintetiza as conclusões do trabalho e propõe direções para desenvolvimentos futuros.

O **Capítulo 7 (Referências Bibliográficas)** lista todas as fontes consultadas durante o desenvolvimento do projeto.

O **Capítulo 8 (Anexos)** inclui materiais complementares como diagramas detalhados, código-fonte relevante e documentação técnica adicional.

---

## REFERÊNCIAS PARCIAIS (Capítulo 1)

IPCC. **Climate Change 2021: The Physical Science Basis**. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change. Cambridge University Press, 2021.

OBSERVATÓRIO DO CLIMA. **Sistema de Estimativas de Emissões de Gases de Efeito Estufa (SEEG)**. Disponível em: https://seeg.eco.br/. Acesso em: 20 out. 2024.

PADGETT, J. P. et al. A comparison of carbon calculators. **Environmental Impact Assessment Review**, v. 28, n. 2-3, p. 106-115, 2008.

PANDEY, D. et al. Carbon footprint: current methods of estimation. **Environmental Monitoring and Assessment**, v. 178, n. 1-4, p. 135-160, 2011.

ROSA, L. P.; SANTOS, M. A. dos. **Inventário de emissões de gases de efeito estufa: metodologias e aplicações no Brasil**. Rio de Janeiro: Interciência, 2019.

WIEDMANN, T.; MINX, J. A definition of 'carbon footprint'. **Ecological Economics Research Trends**, v. 1, p. 1-11, 2008.

WRIGHT, L. A.; KEMP, S.; WILLIAMS, I. 'Carbon footprinting': towards a universally accepted definition. **Carbon Management**, v. 2, n. 1, p. 61-72, 2011.

