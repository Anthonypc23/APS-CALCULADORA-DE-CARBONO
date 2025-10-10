import customtkinter as ctk

ctk.set_appearance_mode('dark')

app = ctk.CTk()

app.title("Calculadora")


app.grid_columnconfigure(1, weight=1)
labelEletro = ctk.CTkLabel(app, text="CTkLabel")
labelEletro.grid(row= 0, column=0, padx=20, pady=20 , sticky="ew")

labelGasolina = ctk.CTkLabel(app, text="CTkLabel")
labelGasolina.grid(row= 0, column=1, padx=20, pady=20 , sticky="ew")

labelaviao = ctk.CTkLabel(app, text="CTkLabel")
labelaviao.grid(row= 0, column=2, padx=20, pady=20 , sticky="ew")

labelCarro = ctk.CTkLabel(app, text="CTkLabel")
labelCarro.grid(row= 0, column=3, padx=20, pady=20 , sticky="ew")


app.geometry('1280x720')

app.mainloop()