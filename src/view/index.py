import customtkinter as ctk


from pydoc import text


def start():
    app.mainloop()

def salvar_valor():
    dados= {}
    dados["eletricidade"] = entryEletro.get()
    dados["Gasolina"] = entryGasolina.get()
    dados["Aviao"] = entryAviao.get()
    dados["Carro"] = entryCarro.get()
    print(dados)
    return dados


def Srelatorio():
    relatorio = ctk.CTkToplevel(app)
    relatorio.title("Relatório")
    relatorio.geometry('800x600')
    
    # Garantir que fique na frente
    relatorio.transient(app)
    relatorio.lift()
    relatorio.focus_force()



ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title("Calculadora")
app.geometry('1280x720')
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

btnCalcular = ctk.CTkButton(app, text="Calcular",font=("Terminal",30,"bold"),width=250, command=salvar_valor)
btnCalcular.grid(row=5,column=1,padx=20,sticky="ew", pady=10)

btnRelatorio = ctk.CTkButton(app, text="Relatorio",font=("Terminal",30,"bold"),width=250, command=Srelatorio)
btnRelatorio.grid(row=5,column=2,padx=20,sticky="ew", pady=10)



