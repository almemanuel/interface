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

        # as listas são utilizadas para separar os dados
        # em suas categorias para que sejam exibidos em ordem
        # ordem: dados[0], email, cel, RA, curso, período, campus, ára, sub-área, qualidades e defeitos
        dados = [[],[],[],[],[],[],[],[],[],[],[]]

        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            dados[0].append(row[0])
            dados[1].append(row[1])
            dados[2].append(row[2])
            dados[3].append(row[3])
            dados[4].append(row[4])
            dados[5].append(row[5])
            dados[6].append(row[6])
            dados[7].append(row[7])
            dados[8].append(row[8])
            dados[9].append(row[9])
            dados[10].append(row[10])

        # aqui cria-se uma nova janela onde os dados são exibidos
        display = tk.Toplevel()
        display.geometry(f"300x{25 * len(dados[0]) + 25}")

        def info(n):
        # essa função mostra mais informações sobre cada participante individualmente

            i = tk.Toplevel()
            i.geometry("500x720")

            candidato = tk.Label(i, text=str(dados[0][n]))
            candidato["font"] = ("Arial", "20", "bold")
            candidato.place(x=40, y=20)

            # essa lista contém argumentos para posicionar os elementos no loop
            args = [80, 110, 140, 170, 200, 230, 260, 290, 320, 420]
            tk.Message(i, text="E-mail:", width=110, font="bold").place(x=15, y=80)
            tk.Message(i, text=str("Whatsapp:"), width=130).place(x=15, y=110)
            tk.Message(i, text=str("RA:"), width=130).place(x=15, y=140)
            tk.Message(i, text=str("Curso:"), width=130).place(x=15, y=170)
            tk.Message(i, text=str("Período:"), width=130).place(x=15, y=200)
            tk.Message(i, text=str("campus:"), width=130).place(x=15, y=230)
            tk.Message(i, text=str("area:"), width=130).place(x=15, y=260)
            tk.Message(i, text=str("Sub-área:"), width=130).place(x=15, y=290)
            tk.Message(i, text=str("Qualidades:"), width=130).place(x=15, y=320)
            tk.Message(i, text=str("Defeitos:"), width=130).place(x=15, y=440)

            py = 80
            for j in range(9):
                tk.Message(i, text=dados[j+1][n], width=340).place(x=125, y=py)
                py += 30

            tk.Message(i, text=dados[10][n], width=340).place(x=125, y=440)

            ## Botoes
            if n != 1:
                tk.Button(i, text="Anterior", width=56, command=lambda:[info(n-1), i.destroy()], bg="lightblue").place(x=10, y=580)
            tk.Button(i, text="Voltar a lista", width=56, command= i.destroy, bg="lightblue").place(x=10, y=610)
            tk.Button(i, text="Sair", width=56, command=quit, bg="lightgreen").place(x=10, y=640)
            if n < len(dados[0]) - 1:
                tk.Button(i, text="Próximo", width=56, command=lambda:[info(n+1), i.destroy()], bg="lightblue").place(x=10, y=670)


        for n in range(len(dados[0])):
            py = n*25
            primeiro_nome = dados[0][n].split(" ")
            if n > 0: tk.Button(display, text=f"{str(primeiro_nome[0])}", width = 25, command=partial(info, n)).place(x=10, y=py)

        file.close()

    def criar():
    # essa função cria um arquivo novo com nome e quantidade de dados
    # definidos pelo usuário e mostra na tela
        try:
            a = str(arqv.get())
            if int(qnt.get()) < 1: raise Exception()

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
