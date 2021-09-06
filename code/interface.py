from tkinter.filedialog import askopenfilenames as dlg
from tkinter.messagebox import showinfo
from itertools import product
import geradorDados as gd
import adicionar
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import csv


class interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("435x350")
        self.frame = tk.Frame(self.root).place()

        self.arqv = tk.StringVar()
        self.qnt = tk.StringVar()
        self.selec = tk.StringVar()

    def info(self, n, dados):
        # essa função mostra mais informações sobre cada participante individualmente
        i = tk.Toplevel()
        i.geometry("525x680")

        candidato = tk.Label(i, text=str(dados[0][n]))
        candidato["font"] = ("Arial", "20", "bold")
        candidato.place(x=40, y=20)

        py = 60
        for j in range(9):
            tk.Message(i, text=dados[j+1][0]+":", width=110).place(x=15, y=py)
            tk.Message(i, text=dados[j+1][n], width=340).place(x=125, y=py)
            py += 25

        tk.Message(i, text=dados[10][0]+":", width=110).place(x=15, y=410)
        tk.Message(i, text=dados[10][n], width=340).place(x=125, y=410)

        # Botoes
        ant = tk.Button(i, text="Anterior", width = 51 if n == len(dados[0]) - 1 else 24, command=lambda:[self.info(n-1, dados), i.destroy()], bg="lightblue")
        voltar = tk.Button(i, text="Voltar a lista", width=52, command= i.destroy, bg="lightblue").place(x=11, y=585)
        sair = tk.Button(i, text="Sair", width=52, command=quit, bg="lightgreen").place(x=11, y=615)
        prox = tk.Button(i, text="Próximo", width = 51 if n == 1 else 24, command=lambda:[self.info(n+1, dados), i.destroy()], bg="lightblue")
        if n == 1:
            prox.place(x=11, y=555)
        elif n < len(dados[0]) - 1:
            ant.place(x=11, y=555)
            prox.place(x=262, y=555)
        else:
            ant.place(x=11, y=555)


    def teste(self):
        texto = self.selec.get()
        print(texto)

    def botoes(self, display, dados):
        px = 20
        count = 0
        for n in range(len(dados[0])):
            primeiro_nome = dados[0][n].split(" ")
            py = n*25
            if n > 21: py = (n - 21*count)*25
            if n % 21 == 0 and n > 0:
                tk.Button(display, text=f"{n} - {str(primeiro_nome[0])}", width = 10, command=lambda:self.info(n, dados)).place(x=px, y=py)
                px += 125
                count += 1
            elif n > 0: tk.Button(display, text=f"{n} - {str(primeiro_nome[0])}", width = 10, command=lambda:self.info(n, dados)).place(x=px, y=py)
            if n < 21: ymax = py + 70

        tk.Button(display, text="Novo", width=7, command=lambda: adicionar.addNovo(dados, str(self.arqv)), bg="lightyellow").place(x=20, y=ymax)
        tk.Button(display, text="Voltar", command=display.destroy, width=7, bg="lightpink").place(x=120, y=ymax)
        #filtro = self.selec
        tk.Label(display, text="Para filtrar, selecione abaixo:").place(x = 20, y = ymax + 35)
        ttk.Combobox(display, textvariable = self.selec, values=["Todos", "Administrativo", "Aviônica", "Mecânica", "Pesquisa e Extensão", "Computação"], width=12).place(x = 20, y = ymax + 65)
        tk.Button(display, text="Filtrar", width = 3, command=self.teste).place(x = 155, y = ymax + 60)


    def abrir(self, f):
    # essa função abre o arquivo especificado pelo usuário
        if type(f) is tuple:
            f = ''.join(f)
            f = f[0:-4]
        try:  # verifica se o nome do arquivo é válido
            file = open(f+'.csv', newline = '')
        except:
            showinfo("arquivo não encontrado", "O arquivo não foi encontrado ou não pode ser exibido. Verifique se o nome está escrito corretamente. \nNOTA: não é necessário incluir '.csv' no nome do arquivo")
            return

        self.arqv = f
        reader = csv.reader(file, delimiter = ',')

        ## alterei pra self, testar depois
        self.dados = [[],[],[],[],[],[],[],[],[],[],[]]
        for row, cont in product(reader, range(0, 11)):
            self.dados[cont].append(row[cont])

        file.close()
        display = tk.Toplevel()
        display.geometry(f"{105 * (len(self.dados[0])//21 if len(self.dados[0]) <= 225 else 10) + 250}x{20 * (len(self.dados[0]) if len(self.dados[0]) < 21 else 25) + 180}")

        self.botoes(display, self.dados)

    def criar(self):
    # essa função cria um arquivo novo com nome e quantidade de dados
    # definidos pelo usuário e mostra na tela
        a = str(self.arqv.get()) if type(self.arqv) is tk.StringVar else str(self.arqv)

        if str(self.qnt.get()) == '':
            showinfo("Quantidada não informada", "Gerando quantidade aleatória de dados.")
            gd.gerar_e_salvar(a)
        elif self.qnt.get().isnumeric():
            gd.gerar_e_salvar(a, int(self.qnt.get()))
        else:
            showinfo("Quantidade inválida", "Impossível gera a quantidade de dados informada. Por favor, digite um valor inteiro ou deixe o campo vazio para uma quantidade aleatória.")
            return
        self.abrir(a)

nw = interface()
def main():
    # essa parte adiciona o menu onde o usuário busca o arquivo
    # existente numa caixa de dialogo que exibe seus arquivos
    exp = tk.Label(nw.frame, text="EXPORTANDO DADOS")
    exp["font"] = ("Arial", "16", "bold")
    exp.place(x=10, y=10)
    tk.Message(nw.frame, text="Clique no botão para localizar o arquivo fonte:", width=470).place(x=10, y=35)
    tk.Button(nw.frame, text="Localizar", width=42, command=lambda:[nw.abrir(dlg())], bg="lightblue").place(x=11, y=60)

    # aqui é possível criar um novo arquivo usando o gerador de gerador de Dados
    sim = tk.Label(nw.frame, text="SIMULADOR")
    sim["font"] = ("Arial", "16", "bold")
    sim.place(x=10, y=110)
    tk.Message(nw.frame, text="Obs: nenhum parametro é obrigatório", width = 500).place(x=10, y=145)
    tk.Message(nw.frame, text="Nome: ", width=40).place(x=10, y=170)
    tk.Message(nw.frame, text="Quantidade: ", width=80).place(x=286, y=170)
    tk.Entry(nw.frame, textvariable=nw.arqv, width = 24).place(x=60, y=170)
    tk.Entry(nw.frame, textvariable=nw.qnt, width=4).place(x=376, y=170)
    tk.Button(nw.frame, text="Criar", width=42, command=nw.criar, bg="lightgreen").place(x=11, y=200)
    tk.Button(nw.frame, text="Fechar", width=42, command=quit, bg="lightpink").place(x=11, y=300)

main()
nw.root.mainloop()
