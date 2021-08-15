import tkinter as tk
import tkinter.messagebox
import geradorDados as gd
import csv

def geral():
# essa função cria elementos gerais e inespecíficos da interface

    root = tk.Tk()
    root.geometry("500x350")
    frame = tk.Frame(root).place()

    def str(s):  # essa função somente corrige as strings
        r = ""
        for i in range(len(s)):
            for j in s[i]:
                if j != '{' and j != '}': r += j
        return r

    def abrir(*arg):
    # essa função abre o arquivo especificado pelo usuário

        # a condicional checa se a função foi chamada pela função criar() para exibir o arquivo recém criado
        if len(arg) != 0: f = arg[0]
        else: f = str(nome.get())

        try:  # verifica se o nome do arquivo é válido
            file = open(f+'.csv', newline = '')
        except:
            tkinter.messagebox.showinfo("arquivo não encontrado", "O arquivo não foi encontrado ou não pode ser exibido. Verifique se o nome está escrito corretamente. \nNOTA: não é necessário incluir '.csv' no nome do arquivo")
            return

        # as listas paralelas são utilizadas para separar os dados
        # em suas categorias para que sejam exibidos em ordem
        nomes = []
        email = []
        cel = []
        ra = []
        curso = []
        periodo = []
        campus = []
        area = []
        subarea = []
        qualidades = []
        defeitos = []

        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            nomes.append(row[0]+'\n')
            email.append(row[1]+'\n')
            cel.append(row[2]+'\n')
            ra.append(row[3]+'\n')
            curso.append(row[4]+'\n')
            periodo.append(row[5]+'\n')
            campus.append(row[6]+'\n')
            area.append(row[7]+'\n')
            subarea.append(row[8]+'\n')
            qualidades.append(row[9]+'\n')
            defeitos.append(row[10]+'\n')

        # aqui cria-se uma nova janela onde os dados são exibidos
        display = tk.Toplevel()
        display.geometry("1340x310")

        tk.Message(display, text=str(nomes), width=210, bg="lightblue").place(x=15, y=40)
        tk.Message(display, text=str(email), width=320, bg="lightgreen").place(x=175, y=40)
        tk.Message(display, text=str(cel), width=260, bg="lightyellow").place(x=465, y=40)
        tk.Message(display, text=str(ra), width=100, bg="lightpink").place(x=635, y=40)
        tk.Message(display, text=str(curso), width=700, bg="lightyellow").place(x=732, y=40)
        tk.Message(display, text=str(periodo), width=60, bg="lightgreen").place(x=1103, y=40)
        tk.Message(display, text=str(campus), width=300, bg="lightblue").place(x=1173, y=40)

        file.close()

    def criar():
    # essa função cria um arquivo novo com nome e quantidade de dados
    # definidos pelo usuário e mostra na tela
        a = str(arqv.get())
        gd.gerar_e_salvar(a, int(qnt.get()))

        abrir(a)

    # essa parte adiciona o menu onde o usuário escreve o nome
    # do arquivo csv que deseja visualizar
    tk.Message(frame, text="Nome do arquivo a ser aberto:", width=500).place(x=150, y=10)
    nome = tk.StringVar()
    a = tk.Entry(frame, textvariable=nome, width=59).place(x=10, y=40)
    b = tk.Button(frame, text="buscar", width=56, command=abrir, bg="lightblue").place(x=10, y=65)

    # aqui é possível criar um novo arquivo usando o gerador de gerador de Dados
    tk.Message(frame, text="criar um novo arquivo:", width=150).place(x=160, y=120)
    tk.Message(frame, text="nome: ", width=70).place(x=10, y=150)
    tk.Message(frame, text="quantidade: ", width=83).place(x=340, y=150)
    arqv = tk.StringVar()
    qnt = tk.IntVar()
    v = tk.Entry(frame, textvariable=arqv, width = 33).place(x=67, y=150)
    q = tk.Entry(frame, textvariable=qnt, width=6).place(x=431, y=150)
    b2 = tk.Button(frame, text="criar", width=56, command=criar, bg="lightgreen").place(x=10, y=175)


    root.mainloop()


geral()
