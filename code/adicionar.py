import tkinter as tk

def bancoDeDados(dados, arqv):
    """cria um arquivo que guardara o resultado final. a cada avaliacao de candidato, ele é reescrito

    Args:
        dados (list): dados após a avaliacao
    """
    candidatos = open(arqv+'.csv', "w")
    for c in range(0, len(dados[0])):
        candidatos.write(f"{dados[0][c].lstrip()}, {dados[1][c].lstrip()}, {dados[2][c].lstrip()}, {dados[3][c].lstrip()}, {dados[4][c].lstrip()}, {dados[5][c].lstrip()}, {dados[6][c].lstrip()}, {dados[7][c].lstrip()}, {dados[8][c].lstrip()}, {dados[9][c].lstrip()}, {dados[10][c].lstrip()}, {dados[11][c].lstrip()}")
        candidatos.write('\n')
    candidatos.close()

def addRes(resultado, dados, indice, arqv):
    """atualiza o resultado da avaliação de acordo com "resultado" e a situação anterior na lista "dados"

    Args:
        resultado (int): 0 ou 1 representando o valor logico recebido
        dados (lista): lista com os dados
        indice (int): indice a ser atualizado
    """
    if resultado == 1:
        if dados[-1][indice] == " Reprovado":
            dados[-1][indice] = "Aprovado"
        else:
            dados[-1][indice] = " Reprovado"
    else:
        if dados[-1][indice] == " Reprovado":
            dados[-1][indice] = " Reprovado"
        else:
            dados[-1][indice] = "Aprovado"
    bancoDeDados(dados, arqv)

def salvar(arqv, infos):
    with open(arqv+".csv", "a") as file:
        for i in range(len(infos)):
            file.write(str(infos[i].get())+",")
        file.write("\n")

    file.close()

def addNovo(dados, arqv):
    window = tk.Toplevel()
    window.geometry("540x480")

    infos = [tk.StringVar() for i in range(11)]

    py = 30
    for d in range(11):
        tk.Message(window, text=dados[d][0], width=200).place(x = 10, y = py)
        tk.Entry(window, textvariable=infos[d], width=50).place(x = 100, y=py)

        py += 30

    tk.Button(window, text="salvar e retornar", width=60, bg="lightblue", command=lambda:[salvar(arqv, infos), window.destroy()]).place(x=10, y=py+40)
    tk.Button(window, text="salvar e adicionar novo", width=60, bg="lightgreen", command=lambda:[salvar(arqv, infos), window.destroy(), addNovo(dados,arqv)]).place(x=10, y=py+70)
