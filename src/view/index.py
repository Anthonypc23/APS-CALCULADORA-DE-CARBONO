import customtkinter as ctk

from utils.index import calc_credito, tratar_dados

def start():
    app.mainloop()

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

def set_resultado(dados):
    if dados:

        valor = calc_credito(dados)

        labelResultado.configure(text=f"{valor['total']:.2f} toneladas de CO2/ano")
    else:
        labelResultado.configure(text="Erro: Entrada inválida. Por favor, insira números válidos.")

def mostrar_compensacao(valores):
    if valores is None:
        labelResultado.configure(text="Por favor, insira números válidos.")
        return
    
    dados = calc_credito(valores)
    
    janela = ctk.CTkToplevel(app)
    janela.title("Sistema de Compensação de Carbono")
    janela.geometry('1400x800')
    janela.grid_columnconfigure(0, weight=1)
    
    # Cabeçalho
    frameHeader = ctk.CTkFrame(janela, fg_color="#8b4513", corner_radius=15)
    frameHeader.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
    
    ctk.CTkLabel(frameHeader, text="SISTEMA DE COMPENSAÇÃO DE CARBONO",
                 font=("Arial", 32, "bold"), text_color="white").pack(pady=15)
    
    ctk.CTkLabel(frameHeader, text=f"Suas emissões anuais: {dados['total']:.2f} toneladas de CO2/ano | {dados['creditos']} créditos necessários",
                 font=("Arial", 18), text_color="#f0e68c").pack(pady=(0, 15))
    
    # Frame scrollável
    frameScroll = ctk.CTkScrollableFrame(janela, fg_color="#2b2b2b", corner_radius=15)
    frameScroll.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
    janela.grid_rowconfigure(1, weight=1)
    
    ctk.CTkLabel(frameScroll, text="AÇÕES DE COMPENSAÇÃO DISPONÍVEIS",
                 font=("Arial", 24, "bold"), text_color="#1f6aa5").pack(pady=20)
    
    # Carregar dados de compensação
    import json
    import os
    
    # Caminho correto para o arquivo JSON
    caminho_json = os.path.join(os.path.dirname(__file__), '..', 'data', 'fatores.json')
    caminho_json = os.path.abspath(caminho_json)
    
    compensacoes = {}
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            fatores = json.load(f)
            compensacoes = fatores.get('compensacao', {})
    except FileNotFoundError:
        try:
            # Tenta caminho alternativo
            caminho_json = 'src/data/fatores.json'
            with open(caminho_json, 'r', encoding='utf-8') as f:
                fatores = json.load(f)
                compensacoes = fatores.get('compensacao', {})
        except Exception as e:
            ctk.CTkLabel(frameScroll, text=f"Erro ao carregar dados de compensação: {str(e)}",
                         font=("Arial", 14), text_color="#ff6b6b").pack(pady=20)
    
    if not compensacoes:
        ctk.CTkLabel(frameScroll, text="Nenhuma ação de compensação disponível.",
                     font=("Arial", 14), text_color="#ffd700").pack(pady=20)
    total_emissao_kg = dados['total'] * 1000  # Converte toneladas para kg
    
    # Criar cards para cada ação
    for key, comp in compensacoes.items():
        frameCard = ctk.CTkFrame(frameScroll, fg_color="#1a1a1a", corner_radius=10)
        frameCard.pack(fill="x", padx=20, pady=10)
        
        # Calcular quantidade necessária (valores já são anuais)
        if 'reducao_kg_ano' in comp:
            reducao_anual = comp['reducao_kg_ano']
            quantidade = int(total_emissao_kg / reducao_anual) + 1 if reducao_anual > 0 else 0
            unidade = "unidades"
            reducao_display = reducao_anual
        elif 'reducao_kg_mes' in comp:
            # Converte para anual (mes * 12)
            reducao_mensal = comp['reducao_kg_mes']
            reducao_anual = reducao_mensal * 12
            quantidade = int(total_emissao_kg / reducao_anual) + 1 if reducao_anual > 0 else 0
            unidade = "unidades"
            reducao_display = reducao_anual
        else:
            reducao_anual = 0
            quantidade = 0
            unidade = "unidades"
            reducao_display = 0
        
        # Título
        ctk.CTkLabel(frameCard, text=f"{comp['nome']}",
                     font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", padx=20, pady=(15, 5))
        
        # Descrição
        if 'descricao' in comp:
            ctk.CTkLabel(frameCard, text=comp['descricao'],
                         font=("Arial", 12, "italic"), text_color="#b0b0b0").pack(anchor="w", padx=40, pady=2)
        
        # Informações
        ctk.CTkLabel(frameCard, text=f"Compensa: {reducao_display:.2f} kg de CO2/ano por unidade",
                     font=("Arial", 14), text_color="#90ee90").pack(anchor="w", padx=40, pady=5)
        
        ctk.CTkLabel(frameCard, text=f"Quantidade necessária para neutralizar suas emissões: {quantidade} {unidade}",
                     font=("Arial", 14, "bold"), text_color="#ffd700").pack(anchor="w", padx=40, pady=(2, 15))
    
    # Botão fechar
    ctk.CTkButton(janela, text="FECHAR", font=("Arial", 18, "bold"),
                  width=200, height=50, fg_color="#8b4513", hover_color="#6b3410",
                  command=janela.destroy).grid(row=2, column=0, pady=20)
    
    janela.transient(app)
    janela.lift()
    janela.focus_force()

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

    # Cabeçalho
    frameHeader = ctk.CTkFrame(relatorio, fg_color="#2d7a3e", corner_radius=15)
    frameHeader.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
    
    ctk.CTkLabel(frameHeader, text="RELATÓRIO DETALHADO DE EMISSÕES ANUAIS",
                 font=("Arial", 32, "bold"), text_color="white").pack(pady=15)
    
    ctk.CTkLabel(frameHeader, text="Análise completa da sua pegada de carbono anual",
                 font=("Arial", 16), text_color="#e0e0e0").pack(pady=(0, 15))

    # Frame scrollável para emissões
    frameScroll = ctk.CTkScrollableFrame(relatorio, fg_color="#2b2b2b", corner_radius=15)
    frameScroll.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
    relatorio.grid_rowconfigure(1, weight=1)
    
    # Título da seção
    ctk.CTkLabel(frameScroll, text="DETALHAMENTO POR CATEGORIA",
                 font=("Arial", 22, "bold"), text_color="#1f6aa5").pack(pady=20)
    
    # Dados de emissão
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
    
    # Total destacado
    frameTotal = ctk.CTkFrame(frameScroll, fg_color="#1a472a", corner_radius=15)
    frameTotal.pack(fill="x", padx=20, pady=20)
    
    ctk.CTkLabel(frameTotal, text="TOTAL DE EMISSÕES ANUAIS",
                 font=("Arial", 24, "bold"), text_color="white").pack(pady=(20, 5))
    
    ctk.CTkLabel(frameTotal, text=f"{dados['total']:.2f} toneladas de CO2/ano",
                 font=("Arial", 32, "bold"), text_color="#90ee90").pack(pady=(5, 20))
    
    # Resumo de compensação
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
    
    ctk.CTkLabel(frameComp, text="Dica: Clique em 'Sistema de Compensação' para ver ações práticas!",
                 font=("Arial", 13, "italic"), text_color="#f0e68c").pack(pady=(15, 20))

    # Botão fechar
    ctk.CTkButton(relatorio, text="FECHAR RELATÓRIO", font=("Arial", 18, "bold"),
                  width=200, height=50, fg_color="#2d7a3e", hover_color="#256832",
                  command=relatorio.destroy).grid(row=2, column=0, pady=20)
    
    # Garantir que fique na frente
    relatorio.transient(app)
    relatorio.lift()
    relatorio.focus_force()

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title("Calculadora de Carbono - Neutralidade Climática")
app.geometry('1600x900')
app.grid_columnconfigure((0,1,2,3,4), weight=1)
app.grid_rowconfigure(0, weight=0)

# Cabeçalho com cor
frameHeader = ctk.CTkFrame(app, fg_color="#1f6aa5", corner_radius=15)
frameHeader.grid(row=0, column=0, columnspan=5, sticky="ew", padx=20, pady=20)

labelH1 = ctk.CTkLabel(frameHeader, text="CALCULADORA DE EMISSÕES DE CO2", 
                       font=("Arial", 38, "bold"), text_color="white")
labelH1.pack(pady=15)

labelSubtitulo = ctk.CTkLabel(frameHeader, text="Calcule sua pegada de carbono e descubra como compensar", 
                              font=("Arial", 16), text_color="#e0e0e0")
labelSubtitulo.pack(pady=(0, 15))

# Frame de Inputs com cor de fundo
frameInputs = ctk.CTkFrame(app, fg_color="#2b2b2b", corner_radius=15)
frameInputs.grid(row=1, column=0, columnspan=5, sticky="ew", padx=20, pady=10)
frameInputs.grid_columnconfigure((0,1,2,3,4), weight=1)

# Título da seção
ctk.CTkLabel(frameInputs, text="DADOS DE CONSUMO", font=("Arial", 20, "bold"), 
             text_color="#1f6aa5").grid(row=0, column=0, columnspan=5, pady=15)

# Primeira linha de inputs com ícones
labelEletro = ctk.CTkLabel(frameInputs, text="Eletricidade\n(kWh/Mês)", 
                           font=("Arial", 13, "bold"), justify="center")
labelEletro.grid(row=1, column=0, padx=10, pady=10)

labelGasolina = ctk.CTkLabel(frameInputs, text="Gasolina\n(L/Dia)", 
                             font=("Arial", 13, "bold"), justify="center")
labelGasolina.grid(row=1, column=1, padx=10, pady=10)

labelaviao = ctk.CTkLabel(frameInputs, text="Avião\n(KM/Mês)", 
                          font=("Arial", 13, "bold"), justify="center")
labelaviao.grid(row=1, column=2, padx=10, pady=10)

labelCarro = ctk.CTkLabel(frameInputs, text="Transporte Público\n(KM/Dia)", 
                          font=("Arial", 13, "bold"), justify="center")
labelCarro.grid(row=1, column=3, padx=10, pady=10)

labelGas = ctk.CTkLabel(frameInputs, text="Gás Natural\n(m³/Mês)", 
                        font=("Arial", 13, "bold"), justify="center")
labelGas.grid(row=1, column=4, padx=10, pady=10)

entryEletro = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                           font=("Arial", 14), justify="center")
entryEletro.grid(row=2, column=0, padx=10, pady=5)

entryGasolina = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                             font=("Arial", 14), justify="center")
entryGasolina.grid(row=2, column=1, padx=10, pady=5)

entryAviao = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                          font=("Arial", 14), justify="center")
entryAviao.grid(row=2, column=2, padx=10, pady=5)

entryCarro = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                          font=("Arial", 14), justify="center")
entryCarro.grid(row=2, column=3, padx=10, pady=5)

entryGas = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                        font=("Arial", 14), justify="center")
entryGas.grid(row=2, column=4, padx=10, pady=5)

# Segunda linha de inputs (centralizados)
labelAgua = ctk.CTkLabel(frameInputs, text="Água\n(m³/Mês)", 
                         font=("Arial", 13, "bold"), justify="center")
labelAgua.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

labelResiduos = ctk.CTkLabel(frameInputs, text="Resíduos\n(kg/Mês)", 
                             font=("Arial", 13, "bold"), justify="center")
labelResiduos.grid(row=3, column=3, padx=10, pady=10)

entryAgua = ctk.CTkEntry(frameInputs, placeholder_text="0", width=300, height=40, 
                         font=("Arial", 14), justify="center")
entryAgua.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

entryResiduos = ctk.CTkEntry(frameInputs, placeholder_text="0", width=140, height=40, 
                             font=("Arial", 14), justify="center")
entryResiduos.grid(row=4, column=3, padx=10, pady=5)

# Frame de Resultado
frameResultado = ctk.CTkFrame(app, fg_color="#1a472a", corner_radius=15)
frameResultado.grid(row=2, column=0, columnspan=5, sticky="ew", padx=20, pady=20)

labelTituloResultado = ctk.CTkLabel(frameResultado, text="TOTAL DE EMISSÕES ANUAIS", 
                                    font=("Arial", 24, "bold"), text_color="white")
labelTituloResultado.pack(pady=(20, 10))

labelResultado = ctk.CTkLabel(frameResultado, text="0.00 toneladas de CO2/ano", 
                              font=("Arial", 36, "bold"), text_color="#90ee90")
labelResultado.pack(pady=(0, 20))

# Frame de Botões
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
