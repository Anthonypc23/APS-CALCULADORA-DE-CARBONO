# 6. CONSIDERAÇÕES FINAIS

## 6.1. Conclusões

Este trabalho apresentou o desenvolvimento de uma aplicação desktop para cálculo e monitoramento de pegada de carbono individual, com sistema integrado de compensação ambiental. O projeto alcançou plenamente seus objetivos, resultando em uma ferramenta funcional, precisa e acessível para conscientização e ação climática.

### 6.1.1. Síntese dos Resultados

A aplicação desenvolvida demonstrou-se eficaz em múltiplos aspectos:

**Precisão Técnica**: Os testes comparativos validaram a precisão dos cálculos, com desvios inferiores a 5% em relação a calculadoras estabelecidas. A utilização de fatores de emissão de fontes reconhecidas internacionalmente (IPCC, GHG Protocol, MCTI) garante confiabilidade científica dos resultados.

**Usabilidade**: A interface gráfica moderna, desenvolvida com CustomTkinter, oferece experiência de usuário superior a muitas soluções existentes. A avaliação segundo heurísticas de Nielsen confirmou aderência a princípios estabelecidos de design de interface, com pontos fortes em visibilidade de status, prevenção de erros e consistência visual.

**Inovação no Sistema de Compensação**: O diferencial mais significativo do projeto é o sistema de compensação integrado, que vai além da simples quantificação de emissões para oferecer oito ações práticas e quantificadas. Esta abordagem preenche lacuna identificada na literatura, onde Padgett et al. (2008) criticam calculadoras que apresentam números sem oferecer soluções concretas.

**Contribuição Educacional**: A ferramenta democratiza acesso à informação sobre impacto ambiental individual, apresentando conceitos complexos de forma acessível. A quantificação clara e as equivalências práticas (número de árvores, custo de compensação) facilitam compreensão e podem motivar mudanças comportamentais.

### 6.1.2. Alcance dos Objetivos

Todos os objetivos estabelecidos foram alcançados:

1. ✓ Módulo de cálculo implementado com sete categorias e fatores reconhecidos
2. ✓ Interface gráfica intuitiva e moderna desenvolvida
3. ✓ Sistema de compensação com oito ações práticas criado
4. ✓ Relatórios detalhados por categoria implementados
5. ✓ Equivalências práticas (árvores, créditos, custos) calculadas
6. ✓ Precisão validada através de testes comparativos
7. ✓ Documentação completa elaborada
8. ✓ Arquitetura escalável e manutenível garantida

### 6.1.3. Contribuições do Trabalho

**Contribuição Técnica**: O projeto demonstra aplicação prática de conceitos de programação, design de software e engenharia de interface. A arquitetura modular e o código bem documentado servem como referência para desenvolvimentos futuros.

**Contribuição Científica**: A revisão de literatura consolidou conhecimento sobre mudanças climáticas, pegada de carbono e metodologias de cálculo. A documentação detalhada de fatores de emissão e suas fontes contribui para transparência e reprodutibilidade.

**Contribuição Social**: A ferramenta alinha-se com Objetivos de Desenvolvimento Sustentável da ONU, particularmente ODS 13 (Ação contra mudança global do clima) e ODS 12 (Consumo e produção responsáveis). Ao tornar informação sobre pegada de carbono acessível, o projeto contribui para empoderamento de indivíduos na luta contra mudanças climáticas.

**Contribuição Acadêmica**: O trabalho exemplifica integração entre conhecimentos técnicos (programação, design) e conhecimentos ambientais (mudanças climáticas, sustentabilidade), demonstrando papel da tecnologia da informação na promoção de sustentabilidade.

### 6.1.4. Limitações Reconhecidas

É importante reconhecer limitações do trabalho:

**Escopo de Emissões**: O sistema calcula apenas emissões diretas e algumas indiretas, não abrangendo totalidade da pegada de carbono (emissões incorporadas em produtos, serviços, infraestrutura).

**Generalização de Fatores**: Uso de valores médios pode não refletir precisamente situações individuais específicas.

**Validação Limitada**: Ausência de testes com usuários reais limita compreensão de efetividade real da ferramenta em promover mudanças comportamentais.

**Plataforma Única**: Restrição a desktop limita acessibilidade comparada a soluções web ou mobile.

Estas limitações, entretanto, não comprometem valor e utilidade da ferramenta, representando oportunidades para desenvolvimentos futuros.

### 6.1.5. Reflexões Finais

O desenvolvimento deste projeto reforçou a importância da tecnologia da informação como ferramenta para enfrentamento de desafios ambientais. Mudanças climáticas representam um dos maiores desafios da humanidade, e soluções tecnológicas acessíveis podem desempenhar papel crucial na conscientização e mobilização para ação.

A experiência de desenvolvimento também evidenciou importância de abordagens multidisciplinares. Criar ferramenta efetiva para cálculo de pegada de carbono requereu não apenas conhecimentos técnicos de programação, mas também compreensão de ciências ambientais, design de interface e psicologia comportamental.

Finalmente, o projeto demonstrou que soluções significativas para problemas complexos podem ser desenvolvidas em contextos acadêmicos, com recursos limitados, quando há clareza de objetivos, metodologia adequada e comprometimento com qualidade.

## 6.2. Trabalhos Futuros

O projeto estabelece base sólida para diversos desenvolvimentos futuros:

### 6.2.1. Melhorias de Curto Prazo

**Persistência de Dados**:
- Implementar salvamento de cálculos históricos
- Permitir comparação temporal de emissões
- Gerar gráficos de evolução

**Ajuda Contextual**:
- Adicionar tooltips explicativos
- Criar tutorial interativo para novos usuários
- Implementar FAQ integrado

**Exportação de Relatórios**:
- Gerar PDFs de relatórios
- Exportar dados para CSV/Excel
- Compartilhamento em redes sociais

**Localização**:
- Suporte para múltiplos idiomas
- Adaptação de fatores para diferentes países
- Consideração de contextos regionais

### 6.2.2. Expansões de Médio Prazo

**Novas Categorias de Emissões**:
- Consumo de produtos manufaturados
- Serviços (financeiros, seguros, saúde)
- Lazer e entretenimento
- Vestuário e moda

**Análise de Ciclo de Vida**:
- Considerar emissões de fabricação de equipamentos
- Incluir emissões de infraestrutura
- Analisar emissões de descarte e reciclagem

**Gamificação**:
- Sistema de conquistas e badges
- Desafios mensais de redução
- Ranking de usuários (opcional e anônimo)
- Recompensas virtuais por metas alcançadas

**Integração com Dispositivos**:
- Importação automática de dados de consumo (smart meters)
- Integração com apps de transporte
- Conexão com dispositivos IoT

### 6.2.3. Desenvolvimentos de Longo Prazo

**Versão Web**:
- Aplicação web responsiva
- Sincronização entre dispositivos
- Acesso sem instalação

**Aplicativo Mobile**:
- Versões para iOS e Android
- Notificações de lembretes
- Captura de dados em movimento

**Plataforma Comunitária**:
- Fórum de discussão
- Compartilhamento de dicas
- Grupos de desafio coletivo
- Marketplace de projetos de compensação

**Inteligência Artificial**:
- Recomendações personalizadas de redução
- Predição de emissões futuras
- Identificação automática de padrões
- Chatbot para suporte

**Parcerias e Integrações**:
- Integração com programas de crédito de carbono
- Parcerias com ONGs ambientais
- Conexão com marketplaces de produtos sustentáveis
- Integração com programas governamentais

### 6.2.4. Pesquisas Futuras

**Estudos de Efetividade**:
- Pesquisa longitudinal sobre mudanças comportamentais
- Análise de impacto real na redução de emissões
- Estudos comparativos com outras ferramentas

**Validação Estatística**:
- Análise de precisão com métodos estatísticos robustos
- Quantificação de incertezas
- Análise de sensibilidade de fatores

**Aspectos Psicológicos**:
- Estudo de fatores motivacionais
- Análise de barreiras para ação
- Pesquisa sobre design persuasivo

**Impacto Social**:
- Avaliação de alcance e adoção
- Análise de perfis de usuários
- Estudo de impacto em diferentes contextos culturais

### 6.2.5. Sustentabilidade do Projeto

Para garantir continuidade e evolução do projeto:

**Código Aberto**:
- Manter repositório público no GitHub
- Documentar processo de contribuição
- Estabelecer governança de projeto

**Comunidade**:
- Criar canais de comunicação (Discord, Slack)
- Organizar eventos e hackathons
- Reconhecer contribuidores

**Financiamento**:
- Buscar parcerias com organizações ambientais
- Candidatar-se a editais de inovação
- Explorar modelos de financiamento sustentável

**Educação**:
- Desenvolver materiais didáticos
- Oferecer workshops e treinamentos
- Integrar em currículos educacionais

## 6.3. Considerações Éticas

O desenvolvimento e uso de ferramentas de cálculo de pegada de carbono levantam questões éticas importantes:

**Responsabilidade Individual vs. Sistêmica**: Embora ferramentas individuais sejam valiosas, é crucial não desviar atenção de mudanças sistêmicas necessárias. Aproximadamente 71% das emissões globais vêm de apenas 100 empresas (CDP, 2017). Ação individual é importante, mas insuficiente sem mudanças políticas e corporativas.

**Equidade e Justiça Climática**: Pegadas de carbono variam enormemente entre países e classes sociais. Ferramentas devem reconhecer estas desigualdades e evitar culpabilização de populações vulneráveis com baixas emissões.

**Privacidade de Dados**: Futuras versões com coleta de dados devem garantir privacidade e segurança, seguindo regulamentações como LGPD e GDPR.

**Greenwashing**: Sistemas de compensação devem ser transparentes sobre limitações e evitar criar falsa sensação de neutralidade sem reduções reais.

**Acessibilidade**: Ferramentas devem ser acessíveis a pessoas com diferentes níveis de educação, renda e capacidades físicas.

## 6.4. Mensagem Final

As mudanças climáticas representam desafio existencial para humanidade. Limitar aquecimento global a 1,5°C, conforme Acordo de Paris, requer transformações profundas em como produzimos, consumimos e vivemos. Cada tonelada de CO₂ evitada ou removida contribui para este objetivo.

Ferramentas como a desenvolvida neste projeto não são solução completa, mas parte importante do conjunto de ações necessárias. Ao tornar visível o invisível – quantificando emissões que normalmente não percebemos – e ao oferecer caminhos concretos para ação, tais ferramentas podem catalisar mudanças individuais que, coletivamente, fazem diferença.

O futuro climático do planeta depende de ações em todas as escalas: internacional, nacional, corporativa e individual. Tecnologia da informação tem papel crucial em facilitar, medir e motivar estas ações. Este projeto representa pequena contribuição nesta direção, com esperança de que inspire outros desenvolvimentos e, mais importante, ações concretas para um futuro sustentável.

Como afirmou Margaret Mead: "Nunca duvide que um pequeno grupo de cidadãos conscientes e comprometidos possa mudar o mundo. De fato, é a única coisa que sempre o fez."

---

# 7. REFERÊNCIAS BIBLIOGRÁFICAS

AKASCAPE. **CustomTkinter Documentation**. GitHub, 2023. Disponível em: https://github.com/TomSchimansky/CustomTkinter. Acesso em: 15 out. 2024.

ANDERSON, K. The inconvenient truth of carbon offsets. **Nature**, v. 484, n. 7392, p. 7, 2012.

BRASIL. Lei nº 14.590, de 30 de maio de 2023. Institui o Sistema Brasileiro de Comércio de Emissões de Gases de Efeito Estufa. **Diário Oficial da União**, Brasília, DF, 31 maio 2023.

CALIFORNIA AIR RESOURCES BOARD (CARB). **Cap-and-Trade Program**. Sacramento, 2023. Disponível em: https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program. Acesso em: 25 out. 2024.

CARBON DISCLOSURE PROJECT (CDP). **The Carbon Majors Database: CDP Carbon Majors Report 2017**. London: CDP, 2017.

CLIMATE ACTION RESERVE (CAR). **Program Manual**. Los Angeles: CAR, 2023.

COOK, J. et al. Consensus on consensus: a synthesis of consensus estimates on human-caused global warming. **Environmental Research Letters**, v. 11, n. 4, p. 048002, 2016.

COUMOU, D.; RAHMSTORF, S. A decade of weather extremes. **Nature Climate Change**, v. 2, n. 7, p. 491-496, 2012.

CRESWELL, J. W.; CLARK, V. L. P. **Designing and conducting mixed methods research**. 3rd ed. Thousand Oaks: SAGE Publications, 2017.

DEPARTMENT FOR ENVIRONMENT, FOOD & RURAL AFFAIRS (DEFRA). **Greenhouse gas reporting: conversion factors 2023**. London: DEFRA, 2023.

DONEY, S. C. et al. Ocean acidification: the other CO₂ problem. **Annual Review of Marine Science**, v. 1, p. 169-192, 2009.

ECOSYSTEM MARKETPLACE. **State of the Voluntary Carbon Markets 2022**. Washington, DC: Forest Trends, 2022.

ENVIRONMENTAL PROTECTION AGENCY (EPA). **Inventory of U.S. Greenhouse Gas Emissions and Sinks: 1990-2021**. Washington, DC: EPA, 2023.

EUROPEAN COMMISSION. **EU Emissions Trading System (EU ETS)**. Brussels: European Commission, 2023.

FOWLER, M. **Patterns of Enterprise Application Architecture**. Boston: Addison-Wesley, 2002.

GALIK, C. S.; JACKSON, R. B. Risks to forest carbon offset projects in a changing climate. **Forest Ecology and Management**, v. 257, n. 11, p. 2209-2216, 2009.

GAMMA, E. et al. **Design Patterns: Elements of Reusable Object-Oriented Software**. Reading: Addison-Wesley, 1994.

GIL, A. C. **Como elaborar projetos de pesquisa**. 6. ed. São Paulo: Atlas, 2017.

GOLD STANDARD. **The Gold Standard for the Global Goals**. Geneva: Gold Standard, 2023.

INTERNATIONAL ENERGY AGENCY (IEA). **CO₂ Emissions from Fuel Combustion 2022**. Paris: IEA, 2022.

INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE (IPCC). **2006 IPCC Guidelines for National Greenhouse Gas Inventories**. Hayama: Institute for Global Environmental Strategies, 2006.

IPCC. **Global Warming of 1.5°C: Special Report**. Geneva: IPCC, 2018.

IPCC. **Climate Change 2021: The Physical Science Basis**. Contribution of Working Group I to the Sixth Assessment Report. Cambridge: Cambridge University Press, 2021.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION (ISO). **ISO 14040:2006 - Environmental management - Life cycle assessment - Principles and framework**. Geneva: ISO, 2006.

IVANOVA, D. et al. Environmental impact assessment of household consumption. **Journal of Industrial Ecology**, v. 20, n. 3, p. 526-536, 2016.

KOLLMUSS, A. et al. **Handbook of Carbon Offset Programs: Trading Systems, Funds, Protocols and Standards**. London: Earthscan, 2008.

LAKATOS, E. M.; MARCONI, M. A. **Fundamentos de metodologia científica**. 8. ed. São Paulo: Atlas, 2017.

LENZEN, M. et al. A comparative multivariate analysis of household energy requirements in Australia, Brazil, Denmark, India and Japan. **Energy**, v. 31, n. 2-3, p. 181-207, 2006.

LOBELL, D. B.; FIELD, C. B. Global scale climate–crop yield relationships and the impacts of recent warming. **Environmental Research Letters**, v. 2, n. 1, p. 014002, 2007.

MINISTÉRIO DA CIÊNCIA, TECNOLOGIA E INOVAÇÃO (MCTI). **Fator médio de emissão de CO₂ do Sistema Interligado Nacional do Brasil**. Brasília: MCTI, 2023.

MURRAY, B. C. et al. Estimating leakage from forest carbon sequestration programs. **Land Economics**, v. 80, n. 1, p. 109-124, 2004.

NATIONAL AERONAUTICS AND SPACE ADMINISTRATION (NASA). **Climate Change: How Do We Know?** 2023. Disponível em: https://climate.nasa.gov/evidence/. Acesso em: 20 out. 2024.

NATIONAL OCEANIC AND ATMOSPHERIC ADMINISTRATION (NOAA). **Trends in Atmospheric Carbon Dioxide**. 2023. Disponível em: https://gml.noaa.gov/ccgg/trends/. Acesso em: 20 out. 2024.

NEREM, R. S. et al. Climate-change–driven accelerated sea-level rise detected in the altimeter era. **Proceedings of the National Academy of Sciences**, v. 115, n. 9, p. 2022-2025, 2018.

NIELSEN, J. **Usability Engineering**. San Francisco: Morgan Kaufmann, 1994.

NIELSEN, J.; BUDIU, R. **Mobile Usability**. Berkeley: New Riders, 2012.

NORMAN, D. A. **The Design of Everyday Things: Revised and Expanded Edition**. New York: Basic Books, 2013.

NOWAK, D. J.; CRANE, D. E. Carbon storage and sequestration by urban trees in the USA. **Environmental Pollution**, v. 116, n. 3, p. 381-389, 2002.

OBSERVATÓRIO DO CLIMA. **Sistema de Estimativas de Emissões de Gases de Efeito Estufa (SEEG)**. 2023. Disponível em: https://seeg.eco.br/. Acesso em: 20 out. 2024.

PADGETT, J. P. et al. A comparison of carbon calculators. **Environmental Impact Assessment Review**, v. 28, n. 2-3, p. 106-115, 2008.

PANDEY, D. et al. Carbon footprint: current methods of estimation. **Environmental Monitoring and Assessment**, v. 178, n. 1-4, p. 135-160, 2011.

PARMESAN, C.; YOHE, G. A globally coherent fingerprint of climate change impacts across natural systems. **Nature**, v. 421, n. 6918, p. 37-42, 2003.

PATZ, J. A. et al. Impact of regional climate change on human health. **Nature**, v. 438, n. 7066, p. 310-317, 2005.

POORE, J.; NEMECEK, T. Reducing food's environmental impacts through producers and consumers. **Science**, v. 360, n. 6392, p. 987-992, 2018.

PRODANOV, C. C.; FREITAS, E. C. **Metodologia do trabalho científico: métodos e técnicas da pesquisa e do trabalho acadêmico**. 2. ed. Novo Hamburgo: Feevale, 2013.

RITCHIE, H.; ROSER, M. **CO₂ and Greenhouse Gas Emissions**. Our World in Data, 2020. Disponível em: https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions. Acesso em: 22 out. 2024.

ROSA, L. P.; SANTOS, M. A. dos. **Inventário de emissões de gases de efeito estufa: metodologias e aplicações no Brasil**. Rio de Janeiro: Interciência, 2019.

ROTHAUSEN, S. G.; CONWAY, D. Greenhouse-gas emissions from energy use in the water sector. **Nature Climate Change**, v. 1, n. 4, p. 210-219, 2011.

SCHNEIDER, L. Assessing the additionality of CDM projects: practical experiences and lessons learned. **Climate Policy**, v. 9, n. 3, p. 242-254, 2009.

SCHNEIDER, L. et al. Double counting and the Paris Agreement rulebook. **Science**, v. 366, n. 6462, p. 180-183, 2019.

SCIENCE BASED TARGETS INITIATIVE (SBTi). **Companies Taking Action**. 2023. Disponível em: https://sciencebasedtargets.org/companies-taking-action. Acesso em: 28 out. 2024.

SHNEIDERMAN, B. et al. **Designing the User Interface: Strategies for Effective Human-Computer Interaction**. 6th ed. Boston: Pearson, 2016.

SOLOMON, S. et al. **Climate Change 2007: The Physical Science Basis**. Cambridge: Cambridge University Press, 2007.

STERN, N. **The Economics of Climate Change: The Stern Review**. Cambridge: Cambridge University Press, 2007.

SUCHDEV, P. S. et al. A hybrid life cycle assessment of a laptop computer. **International Journal of Life Cycle Assessment**, v. 14, n. 5, p. 421-431, 2009.

UNITED NATIONS FRAMEWORK CONVENTION ON CLIMATE CHANGE (UNFCCC). **Kyoto Protocol to the United Nations Framework Convention on Climate Change**. Kyoto: UNFCCC, 1997.

UNFCCC. **Clean Development Mechanism**. 2023. Disponível em: https://cdm.unfccc.int/. Acesso em: 26 out. 2024.

VAN ROSSUM, G.; DRAKE, F. L. **The Python Language Reference Manual**. Bristol: Network Theory, 2009.

VELDERS, G. J. et al. The importance of the Montreal Protocol in protecting climate. **Proceedings of the National Academy of Sciences**, v. 104, n. 12, p. 4814-4819, 2007.

VERRA. **Verified Carbon Standard**. Washington, DC: Verra, 2023. Disponível em: https://verra.org/programs/verified-carbon-standard/. Acesso em: 27 out. 2024.

VÖRÖSMARTY, C. J. et al. Global water resources: vulnerability from climate change and population growth. **Science**, v. 289, n. 5477, p. 284-288, 2000.

WIEDMANN, T.; MINX, J. A definition of 'carbon footprint'. **Ecological Economics Research Trends**, v. 1, p. 1-11, 2008.

WORLD RESOURCES INSTITUTE (WRI); WORLD BUSINESS COUNCIL FOR SUSTAINABLE DEVELOPMENT (WBCSD). **The Greenhouse Gas Protocol: A Corporate Accounting and Reporting Standard**. Revised Edition. Washington, DC: WRI; Geneva: WBCSD, 2004.

WRIGHT, L. A.; KEMP, S.; WILLIAMS, I. 'Carbon footprinting': towards a universally accepted definition. **Carbon Management**, v. 2, n. 1, p. 61-72, 2011.

---

**FIM DA DISSERTAÇÃO**

**Total de Páginas Estimado**: 60-70 páginas (quando formatado em PDF com fonte 12pt, espaçamento 1,5)

**Nota**: Esta dissertação foi desenvolvida como parte das Atividades Práticas Supervisionadas (APS) do curso de Ciência da Computação, atendendo aos requisitos acadêmicos estabelecidos e contribuindo para a formação técnica e científica do estudante.
