import tkinter as tk
from tkinter import ttk

# Janela  primcipal
janela = tk.Tk()
janela.title("Interface Avançada")
janela.geometry("400x500")

# Criar caixa entrada
label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

# Criar botões de radio
label_preferencia = tk.Label(janela, text="Digite sua preferência")
label_preferencia.pack(pady=5)
var_radio = tk.StringVar(value="Café")
radio_cafe = tk.Radiobutton(janela, text="Café", variable=var_radio, value="Café")
radio_cha = tk.Radiobutton(janela, text="Chá", variable=var_radio, value="Chá")
radio_suco = tk.Radiobutton(janela, text="Suco", variable=var_radio, value="Suco")
radio_agua = tk.Radiobutton(janela, text="Água", variable=var_radio, value="Água")
radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()


# Executar a janela principal
janela.mainloop()
