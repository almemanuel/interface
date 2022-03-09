from tkinter.filedialog import askopenfilenames as dlg
from tkinter.messagebox import showinfo
from itertools import product
from functools import partial
import geradorDados as gd
from tkinter import ttk
import tkinter as tk
import adicionar
import csv
import sys

def quit():
    sys.exit()


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
        i.geometry("525x700")

        candidato = tk.Label(i, text=str(dados[0][n]))
        candidato["font"] = ("Arial", "20", "bold")
        candidato.place(x=40, y=20)

        py = 60
        for j in range(9):
            tk.Message(i, text=dados[j+1][0]+":", width=110).place(x=15, y=py)
            tk.Message(i, text=dados[j+1][n], width=340).place(x=125, y=py)
            py += 25

        tk.Message(i, text=dados[-2][0]+":", width=110).place(x=15, y=410)
        tk.Message(i, text=dados[-2][n], width=340).place(x=125, y=410)

        resultado = tk.IntVar()
        tk.Message(i, text="MARCAR A CAIXA SE O CANDIDATO FOR APTO", width=340).place(x=10, y=565)

        if dados[-1][n] == " Reprovado": tk.Checkbutton(i, width=3, variable=resultado, onvalue = 1, offvalue = 0).place(x=420, y=565)
        else: tk.Checkbutton(i, width=3, variable=resultado, onvalue = 0, offvalue = 1).place(x=420, y=565)

        # Botoes
        ant = tk.Button(i, text="Anterior", width = 52 if n == len(dados[0]) - 1 else 24, command=lambda:[adicionar.addRes(resultado.get(), dados, n,self.arqv), self.info(n-1, dados), i.destroy()], bg="lightblue")
        voltar = tk.Button(i, text="Voltar a lista", width=52, command= lambda:[adicionar.addRes(resultado.get(), dados, n, self.arqv), i.destroy()], bg="lightblue").place(x=11, y=630)
        sair = tk.Button(i, text="Sair", width=52, command=lambda:[adicionar.addRes(resultado.get(), dados, n, self.arqv), quit()], bg="lightgreen").place(x=11, y=660)
        prox = tk.Button(i, text="Próximo", width = 52 if n == 1 else 24, command=lambda:[adicionar.addRes(resultado.get(), dados, n, self.arqv), self.info(n+1, dados), i.destroy()], bg="lightblue")
        if len(dados[0]) != 2:
            if n == 1:
                prox.place(x=11, y=600)
            elif n < len(dados[0]) - 1:
                ant.place(x=11, y=600)
                prox.place(x=262, y=600)
            else:
                ant.place(x=11, y=600)

    def botoes(self, display, dados, bool):
        px = 20
        count = 0
        for n in range(len(dados[0])):
            primeiro_nome = dados[0][n].split(" ")
            py = n*25
            if n > 21: py = (n - 21*count)*25
            if n > 0: tk.Button(display, text=f"{n} - {str(primeiro_nome[0])}", width = 10, command=partial(self.info, n, dados)).place(x=px, y=py)
            if n % 21 == 0 and n > 0:
                px += 125
                count += 1
            if n < 21: ymax = py + 70

        tk.Button(display, text="Novo", width=7, command=lambda: adicionar.addNovo(dados, str(self.arqv)), bg="lightyellow").place(x=20, y=ymax)
        tk.Button(display, text="Voltar", command=display.destroy, width=7, bg="lightpink").place(x=120, y=ymax)

        if bool:
            tk.Label(display, text="Para filtrar, selecione abaixo:").place(x = 20, y = ymax + 35)
            ttk.Combobox(display, textvariable = self.selec, values=["Administrativo", "Aviônica", "Mecânica", "Pesquisa e Extensão", "Computação"], width=12).place(x = 20, y = ymax + 65)
            tk.Button(display, text="Filtrar", width = 3, command=lambda: self.filtro(dados)).place(x = 155, y = ymax + 60)

    def abrir(self, dados, msg = "Todos os candidatos"):
        display = tk.Toplevel()
        display.geometry(f"{105 * (len(dados[0])//21 if len(dados[0]) <= 225 else 10) + 250}x{20 * (len(dados[0]) if len(dados[0]) < 21 else 25) + 200}")

        titulo = tk.Label(display, text=msg)
        titulo["font"] = ("Arial", "15", "bold")
        titulo.place(x=20, y=0)

        self.botoes(display, dados, False if msg != "Todos os candidatos" else True)

    def filtro(self, dados):
        filtrados = []
        for dado in range(len(dados[0])):
            a = str(dados[7][dado])
            if str(a[1:len(a)]) == str(self.selec.get()): filtrados.append(dado)
        ndados = [[] for i in range(12)]

        for a in range(12):
            ndados[a].append(dados[a][0])
            for b in filtrados:
                ndados[a].append(dados[a][b])

        self.abrir(ndados, self.selec.get())

    def gerarDados(self, f):
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

        dados = [[] for i in range(12)]
        for row, cont in product(reader, range(0, 12)):
            dados[cont].append(row[cont])

        file.close()
        self.abrir(dados)


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
            showinfo("Quantidade inválida", "Impossível gerar a quantidade de dados informada. Por favor, digite um valor inteiro ou deixe o campo vazio para uma quantidade aleatória.")
            return
        self.gerarDados(a)

nw = interface()
def main():
    # essa parte adiciona o menu onde o usuário busca o arquivo
    # existente numa caixa de dialogo que exibe seus arquivos
    exp = tk.Label(nw.frame, text="EXPORTANDO DADOS")
    exp["font"] = ("Arial", "16", "bold")
    exp.place(x=10, y=10)
    tk.Message(nw.frame, text="Clique no botão para localizar o arquivo fonte:", width=470).place(x=10, y=35)
    tk.Button(nw.frame, text="Localizar", width=42, command=lambda:[nw.gerarDados(dlg())], bg="lightblue").place(x=11, y=60)

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
