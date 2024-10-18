import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Criar Senha")

def calculate():
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    especiais = '!@#$%&?*/'
    numeros = "0123456789"

    caracteres = alfabeto + numeros + especiais
    senha = ''
    
    for i in range(8):
        senha += random.choice(caracteres)
    
    Senha.set(senha)  # Atualiza o StringVar com a senha gerada

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

Senha = StringVar()
ttk.Label(mainframe, textvariable=Senha).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Gerar senha", command=calculate).grid(column=1, row=2, sticky=W)

root.mainloop()