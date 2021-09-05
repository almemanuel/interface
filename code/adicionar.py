import tkinter as tk


def salvar(arqv, infos):
    with open(arqv+".csv", "a") as file:
        for i in range(len(infos)):
            file.write(str(infos[i].get())+",")
        file.write("\n")

    file.close()

def addNovo(dados, arqv):
    window = tk.Toplevel()
    window.geometry("540x480")

    infos = []
    for i in range(11): infos.append(tk.StringVar())

    py = 30
    for d in range(11):
        tk.Message(window, text=dados[d][0], width=200).place(x = 10, y = py)
        tk.Entry(window, textvariable=infos[d], width=50).place(x = 100, y=py)

        py += 30

    tk.Button(window, text="salvar e retornar", width=60, bg="lightblue", command=lambda:[salvar(arqv, infos), window.destroy()]).place(x=10, y=py+40)
    tk.Button(window, text="salvar e adicionar novo", width=60, bg="lightgreen", command=lambda:[salvar(arqv, infos), window.destroy(), addNovo(dados,arqv)]).place(x=10, y=py+70)
