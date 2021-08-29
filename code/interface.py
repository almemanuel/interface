from tkinter.messagebox import showinfo
from functools import partial
import geradorDados as gd
import tkinter as tk
import csv
from itertools import product

class interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("435x350")
        self.frame = tk.Frame(self.root).place()

        self.nome = tk.StringVar()
        self.arqv = tk.StringVar()
        self.qnt = tk.StringVar()
        self.dados = [[],[],[],[],[],[],[],[],[],[],[]]

    def info(self, n):
        # essa função mostra mais informações sobre cada participante individualmente

        i = tk.Toplevel()
        i.geometry("525x680")

        candidato = tk.Label(i, text=str(self.dados[0][n]))
        candidato["font"] = ("Arial", "20", "bold")
        candidato.place(x=40, y=20)

        py = 60
        for j in range(9):
            tk.Message(i, text=self.dados[j+1][0]+":", width=110).place(x=15, y=py)
            tk.Message(i, text=self.dados[j+1][n], width=340).place(x=125, y=py)
            py += 25

        tk.Message(i, text=self.dados[10][0]+":", width=110).place(x=15, y=410)
        tk.Message(i, text=self.dados[10][n], width=340).place(x=125, y=410)

        # Botoes
        ant = tk.Button(i, text="Anterior", width = 51 if n == len(self.dados[0]) - 1 else 24, command=lambda:[self.info(n-1), i.destroy()], bg="lightblue")
        voltar = tk.Button(i, text="Voltar a lista", width=52, command= i.destroy, bg="lightblue")
        sair = tk.Button(i, text="Sair", width=52, command=quit, bg="lightgreen")
        prox = tk.Button(i, text="Próximo", width = 51 if n == 1 else 24, command=lambda:[self.info(n+1), i.destroy()], bg="lightblue")
        if n == 1:
            prox.place(x=11, y=555)
        elif n < len(self.dados[0]) - 1:
            ant.place(x=11, y=555)
            prox.place(x=262, y=555)
        else:
            ant.place(x=11, y=555)

        voltar.place(x=11, y=585)
        sair.place(x=11, y=615)


    def botoes(self, display):

        px = 10
        count = 0
        for n in range(len(self.dados[0])):
            py = n*25
            primeiro_nome = self.dados[0][n].split(" ")

            if n % 19 == 0 and n >0:
                px += 110
                py = 25
                count += 1
            if n > 19: py = (n - 19*count)*25
            if n > 0: tk.Button(display, text=f"{str(primeiro_nome[0])}", width = 10, command=partial(self.info, n)).place(x=px, y=py)

    def abrir(self, *arg):
    # essa função abre o arquivo especificado pelo usuário

        # a condicional checa se a função foi chamada pela função criar() para exibir o arquivo recém criado
        if len(arg) != 0: f = arg[0]
        else: f = str(self.nome.get())

        try:  # verifica se o nome do arquivo é válido
            file = open(f+'.csv', newline = '')
        except:
            showinfo("arquivo não encontrado", "O arquivo não foi encontrado ou não pode ser exibido. Verifique se o nome está escrito corretamente. \nNOTA: não é necessário incluir '.csv' no nome do arquivo")
            return

        reader = csv.reader(file, delimiter = ',')

        for row, cont in product(reader, range(0, 11)):
            self.dados[cont].append(row[cont])

        display = tk.Toplevel()
        display.geometry(f"{125 * (len(self.dados[0])//19) + 120}x500")

        self.botoes(display)

    def criar(self):
    # essa função cria um arquivo novo com nome e quantidade de dados
    # definidos pelo usuário e mostra na tela
        a = str(self.arqv.get())
        if str(self.qnt.get()) == '':
            showinfo("Quantidada não informada", "Gerando quantidade aleatória de dados.")
            gd.gerar_e_salvar(a)
        elif self.qnt.get().isnumeric() and int(self.qnt.get()):
            gd.gerar_e_salvar(a, int(self.qnt.get()))
        else:
            showinfo("Quantidade inválida", "Impossível gera a quantidade de dados informada. Por favor, digite um valor inteiro não nulo ou deixe o campo vazio para uma quantidade aleatória.")
            return
        self.abrir(a)


nw = interface()
def main():
    # essa parte adiciona o menu onde o usuário escreve o nome
    # do arquivo csv que deseja visualizar
    tk.Message(nw.frame, text="Nome do arquivo a ser aberto:", width=470).place(x=10, y=10)
    tk.Entry(nw.frame, textvariable=nw.nome, width=45).place(x=10, y=35)
    tk.Button(nw.frame, text="Buscar", width=42, command=nw.abrir, bg="lightblue").place(x=11, y=60)

    # aqui é possível criar um novo arquivo usando o gerador de gerador de Dados
    tk.Message(nw.frame, text="SIMULADOR:", width=500).place(x=10, y=120)
    tk.Message(nw.frame, text="Nenhum parametro é obrigatório", width = 500).place(x=10, y=145)
    tk.Message(nw.frame, text="Nome: ", width=40).place(x=10, y=170)
    tk.Message(nw.frame, text="Quantidade: ", width=80).place(x=286, y=170)
    tk.Entry(nw.frame, textvariable=nw.arqv, width = 24).place(x=60, y=170)
    tk.Entry(nw.frame, textvariable=nw.qnt, width=4).place(x=376, y=170)
    tk.Button(nw.frame, text="Criar", width=42, command=nw.criar, bg="lightgreen").place(x=11, y=200)
    tk.Button(nw.frame, text="Fechar", width=42, command=quit, bg="lightpink").place(x=11, y=300)

main()
nw.root.mainloop()
