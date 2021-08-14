import tkinter as tk
import csv as csv
import tkinter.messagebox

def geral():
# essa função cria elementos gerais e inespecíficos da interface

    root = tk.Tk()
    root.geometry("500x350")
    frame = tk.Frame(root).place()


    def abrir():
    # essa função abre o arquivo especificado pelo usuário

        try:  # verifica se o nome do arquivo é válido
            arquivo = open(str(nome.get())+'.csv', "r")
        except:
            tkinter.messagebox.alert("arquivo não encontrado", "O arquivo que você procurou não foi encontrado. Verifique se o nome está escrito corretamente. \nNOTA: não é necessário incluir '.csv' no nome do arquivo")
            return

        # aqui cria-se uma nova janela onde os dados são exibidos
        display = tk.Toplevel()
        display.geometry("1200x540")

        dados = []
        py = 10
        c = 0
        for i in arquivo:
            tk.Message(display, text=i, width=1150).place(x=10, y=py)
            py += 90

    # essa parte adiciona o menu onde o usuário escreve o nome
    # do arquivo csv que deseja visualizar
    ma = tk.Message(frame, text="Nome do arquivo a ser aberto:", width=500).place(x=150, y=10)
    nome = tk.StringVar()
    a = tk.Entry(frame, textvariable=nome, width=59).place(x=10, y=40)
    b = tk.Button(frame, text="buscar", width=56, command=abrir).place(x=10, y=65)

    root.mainloop()

geral()
