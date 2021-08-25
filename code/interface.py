import tkinter as tk
import tkinter.messagebox
import geradorDados as gd
import csv
from functools import partial
def geral():
# essa função cria elementos gerais e inespecíficos da interface

    root = tk.Tk()
    root.geometry("435x350")
    frame = tk.Frame(root).place()

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
            nomes.append(row[0])
            email.append(row[1])
            cel.append(row[2])
            ra.append(row[3])
            curso.append(row[4])
            periodo.append(row[5])
            campus.append(row[6])
            area.append(row[7])
            subarea.append(row[8])
            qualidades.append(row[9])
            defeitos.append(row[10])

        # aqui cria-se uma nova janela onde os dados são exibidos
        display = tk.Toplevel()
        display.geometry(f"300x{25 * len(nomes) + 25}")

        def info(n):
        # essa função mostra mais informações sobre cada participante individualmente

            i = tk.Toplevel()
            i.geometry("500x720")

            candidato = tk.Label(i, text=str(nomes[n]))
            candidato["font"] = ("Arial", "20", "bold")
            candidato.place(x=40, y=20)

            tk.Message(i, text="E-mail:", width=110, font="bold").place(x=15, y=80)
            tk.Message(i, text=str(email[n]), width=400).place(x=125, y=80)
            tk.Message(i, text=str("Whatsapp:"), width=130).place(x=15, y=110)
            tk.Message(i, text=str(cel[n]), width=400).place(x=125, y=110)
            tk.Message(i, text=str("RA:"), width=130).place(x=15, y=140)
            tk.Message(i, text=str(ra[n]), width=400).place(x=125, y=140)
            tk.Message(i, text=str("Curso:"), width=130).place(x=15, y=170)
            tk.Message(i, text=str(curso[n]), width=1000).place(x=125, y=170)
            tk.Message(i, text=str("Período:"), width=130).place(x=15, y=200)
            tk.Message(i, text=str(periodo[n]), width=1000).place(x=125, y=200)
            tk.Message(i, text=str("campus:"), width=130).place(x=15, y=230)
            tk.Message(i, text=str(campus[n]), width=1000).place(x=125, y=230)
            tk.Message(i, text=str("area:"), width=130).place(x=15, y=260)
            tk.Message(i, text=str(area[n]), width=1000).place(x=125, y=260)
            tk.Message(i, text=str("Sub-área:"), width=130).place(x=15, y=290)
            tk.Message(i, text=str(subarea[n]), width=1000).place(x=125, y=290)
            tk.Message(i, text=str("Qualidades:"), width=130).place(x=15, y=320)
            tk.Message(i, text=str(qualidades[n]), width=340).place(x=125, y=320)
            tk.Message(i, text=str("Defeitos:"), width=130).place(x=15, y=410)
            tk.Message(i, text=str(defeitos[n]), width=340).place(x=125, y=420)

            ## Botoes
            if n != 1:
                tk.Button(i, text="Anterior", width=50, command=lambda:[info(n-1), i.destroy()], bg="lightblue").place(x=10, y=580)
            tk.Button(i, text="Voltar a lista", width=50, command= i.destroy, bg="lightblue").place(x=10, y=610)
            tk.Button(i, text="Sair", width=50, command=quit, bg="lightgreen").place(x=10, y=640)
            if n < len(nomes) - 1:
                tk.Button(i, text="Próximo", width=50, command=lambda:[info(n+1), i.destroy()], bg="lightblue").place(x=10, y=670)


        for n in range(len(nomes)):
            py = n*25
            primeiro_nome = nomes[n].split(" ")
            if n > 0: tk.Button(display, text=f"{str(primeiro_nome[0])}", width = 25, command=partial(info, n)).place(x=10, y=py)

        file.close()

    def criar():
    # essa função cria um arquivo novo com nome e quantidade de dados
    # definidos pelo usuário e mostra na tela
        try:
            if int(qnt.get()) < 1: raise Exception()
            a = str(arqv.get())

            gd.gerar_e_salvar(a, int(qnt.get()))
            abrir(a)
        except:
            tkinter.messagebox.showinfo("entrada inválida", "Impossível criar arquivo. Verifique se a quantidade e o nome estão corretos.")

    # essa parte adiciona o menu onde o usuário escreve o nome
    # do arquivo csv que deseja visualizar
    tk.Message(frame, text="Nome do arquivo a ser aberto:", width=470).place(x=10, y=10)
    nome = tk.StringVar()
    a = tk.Entry(frame, textvariable=nome, width=50).place(x=10, y=35)
    b = tk.Button(frame, text="Buscar", width=47, command=abrir, bg="lightblue").place(x=11, y=60)

    # aqui é possível criar um novo arquivo usando o gerador de gerador de Dados
    tk.Message(frame, text="Novo do arquivo a ser gerado:", width=500).place(x=10, y=120)
    tk.Message(frame, text="Nome: ", width=40).place(x=10, y=145)
    tk.Message(frame, text="Quantidade: ", width=80).place(x=286, y=145)
    arqv = tk.StringVar()
    qnt = tk.IntVar()
    v = tk.Entry(frame, textvariable=arqv, width = 28).place(x=60, y=145)
    q = tk.Entry(frame, textvariable=qnt, width=5).place(x=376, y=145)
    b2 = tk.Button(frame, text="Criar", width=47, command=criar, bg="lightgreen").place(x=11, y=170)
    tk.Button(frame, text="Fechar", width=47, command=quit, bg="lightpink").place(x=11, y=300)


    root.mainloop()


geral()
