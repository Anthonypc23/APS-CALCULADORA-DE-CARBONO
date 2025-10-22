import customtkinter as ctk

from utils.index import calc_credito, tratar_dados

def start():
    app.mainloop()

def get_valores():

    dados_tratados = tratar_dados({
        "eletricidade": entryEletro.get(),
        "combustivel": entryGasolina.get(),
        "voo": entryAviao.get(),
        "transporte": entryCarro.get()
    })

    return dados_tratados

def set_resultado(dados):
    if dados:

        valor = calc_credito(dados)

        labelH2.configure(text=f"{valor['total']:.2f} toneladas de CO²")
    else:
        labelH2.configure(text="Erro: Entrada inválida. Por favor, insira números válidos.")

def Srelatorio():
    valores = get_valores()
    dados = calc_credito(valores)

    if valores is None:
        labelH2.configure(text="Por favor, insira números válidos.")
        return

    relatorio = ctk.CTkToplevel(app)
    relatorio.title("Relatório")
    relatorio.geometry('1280x300')
    relatorio.grid_columnconfigure((0,1,2,3), weight=1)

    labelH1 = ctk.CTkLabel(relatorio, text="Extrato de CO2", font=("Terminal", 30,"bold"))
    labelH1.grid(row=0, column= 1, pady = 20, sticky= "ew", columnspan=2)

    TituloEletro = ctk.CTkLabel(relatorio, text="Eletricidade kwh/Mês:" , font=("Terminal", 20, "bold"))
    TituloEletro.grid(row= 1, column=0, padx=20, pady=20 , sticky="ew")

    TituloGasolina = ctk.CTkLabel(relatorio, text="Gasolina Litros/Dia:", font=("Terminal", 20, "bold"))
    TituloGasolina.grid(row= 1, column=1, padx=20, pady=20 , sticky="ew")

    Tituloaviao = ctk.CTkLabel(relatorio, text="Avião KM/Mês:", font=("Terminal", 20, "bold"))
    Tituloaviao.grid(row= 1, column=2, padx=20, pady=20 , sticky="ew")

    TituloCarro = ctk.CTkLabel(relatorio, text="Transporte Publico KM/Dia:", font=("Terminal", 20, "bold"))
    TituloCarro.grid(row= 1, column=3, padx=20, pady=20 , sticky="ew")

    ResultadoEletro = ctk.CTkLabel(relatorio, text=dados['eletricidade'] , font=("Terminal", 20, "bold"))
    ResultadoEletro.grid(row= 2, column=0, padx=20, pady=20 , sticky="ew")

    ResultadoGasolina = ctk.CTkLabel(relatorio, text=dados['combustivel'], font=("Terminal", 20, "bold"))
    ResultadoGasolina.grid(row= 2, column=1, padx=20, pady=20 , sticky="ew")

    Resultadoaviao = ctk.CTkLabel(relatorio, text=dados['voo'], font=("Terminal", 20, "bold"))
    Resultadoaviao.grid(row= 2, column=2, padx=20, pady=20 , sticky="ew")

    ResultadoCarro = ctk.CTkLabel(relatorio, text=dados['Transporte'], font=("Terminal", 20, "bold"))
    ResultadoCarro.grid(row= 2, column=3, padx=20, pady=20 , sticky="ew")

    tituloTotal = ctk.CTkLabel(relatorio, text=f"Total de Creditos: {dados['total']:.2f}",font=("Terminal",30,"bold"),width=250)
    tituloTotal.grid(row=5,column=1,padx=20,sticky="ew", pady=10, columnspan= 2)

    
    # Garantir que fique na frente
    relatorio.transient(app)
    relatorio.lift()
    relatorio.focus_force()

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title("Calculadora")
app.geometry('1280x500')
app.grid_columnconfigure((0,1,2,3), weight=1)

labelH1 = ctk.CTkLabel(app, text="Digite a media de Consumo em Cada Categoria", font=("Terminal", 30,"bold"))
labelH1.grid(row=0, column= 1, pady = 20, sticky= "ew", columnspan=2)

labelEletro = ctk.CTkLabel(app, text="Eletricidade kwh/Mês:" , font=("Terminal", 20, "bold"))
labelEletro.grid(row= 1, column=0, padx=20, pady=20 , sticky="ew")

labelGasolina = ctk.CTkLabel(app, text="Gasolina Litros/Dia:", font=("Terminal", 20, "bold"))
labelGasolina.grid(row= 1, column=1, padx=20, pady=20 , sticky="ew")

labelaviao = ctk.CTkLabel(app, text="Avião KM/Mês:", font=("Terminal", 20, "bold"))
labelaviao.grid(row= 1, column=2, padx=20, pady=20 , sticky="ew")

labelCarro = ctk.CTkLabel(app, text="Transporte Publico KM/Dia:", font=("Terminal", 20, "bold"))
labelCarro.grid(row= 1, column=3, padx=20, pady=20 , sticky="ew")

entryEletro = ctk.CTkEntry(app)
entryEletro.grid(row=2, column=0)

entryGasolina = ctk.CTkEntry(app)
entryGasolina.grid(row=2, column=1)

entryAviao = ctk.CTkEntry(app)
entryAviao.grid(row=2, column=2)

entryCarro = ctk.CTkEntry(app)
entryCarro.grid(row=2, column=3)

labelH2 = ctk.CTkLabel(app, text="TOTAL CO²", font=("Terminal",30,"bold"))
labelH2.grid(row=3,column=1,padx=20,sticky="ew", pady=40 , columnspan=2)

labelH2 = ctk.CTkLabel(app, text="0", font=("Terminal",30,"bold"))
labelH2.grid(row=4,column=1,padx=20,sticky="ew", pady=10 , columnspan=2)

btnCalcular = ctk.CTkButton(app, text="Calcular",font=("Terminal",30,"bold"),width=250, command=lambda: set_resultado(get_valores()))
btnCalcular.grid(row=5,column=1,padx=20,sticky="ew", pady=10)

btnRelatorio = ctk.CTkButton(app, text="Relatorio",font=("Terminal",30,"bold"),width=250, command=Srelatorio)
btnRelatorio.grid(row=5,column=2,padx=20,sticky="ew", pady=10)
