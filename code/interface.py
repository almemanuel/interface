import tkinter as tk
import tkinter.messagebox
import csv

def geral():
# essa função cria elementos gerais e inespecíficos da interface

    root = tk.Tk()
    root.geometry("500x350")
    frame = tk.Frame(root).place()


    def abrir():
    # essa função abre o arquivo especificado pelo usuário

        try:  # verifica se o nome do arquivo é válido
            file = open(str(nome.get())+'.csv', newline = '')
        except:
            tkinter.messagebox.showinfo("arquivo não encontrado", "O arquivo que você procurou não foi encontrado. Verifique se o nome está escrito corretamente. \nNOTA: não é necessário incluir '.csv' no nome do arquivo")
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
        display.geometry("1300x310")

        tk.Message(display, text=nomes, width=210, bg="lightblue").place(x=15, y=40)
        tk.Message(display, text=email, width=320, bg="lightgreen").place(x=175, y=40)
        tk.Message(display, text=cel, width=260, bg="lightyellow").place(x=465, y=40)
        tk.Message(display, text=ra, width=100, bg="lightpink").place(x=635, y=40)
        tk.Message(display, text=curso, width=600, bg="lightyellow").place(x=732, y=40)
        tk.Message(display, text=periodo, width=60, bg="lightgreen").place(x=1043, y=40)
        tk.Message(display, text=campus, width=300, bg="lightblue").place(x=1109, y=40)

    # essa parte adiciona o menu onde o usuário escreve o nome
    # do arquivo csv que deseja visualizar
    ma = tk.Message(frame, text="Nome do arquivo a ser aberto:", width=500).place(x=150, y=10)
    nome = tk.StringVar()
    a = tk.Entry(frame, textvariable=nome, width=59).place(x=10, y=40)
    b = tk.Button(frame, text="buscar", width=56, command=abrir).place(x=10, y=65)

    root.mainloop()

geral()
