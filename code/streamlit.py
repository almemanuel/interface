import streamlit as st
import pandas as pd
import csv

st.title("candidatos")

def read(f):
	of = csv.reader(f, delimiter=",")

	dados = [[],[],[],[],[],[],[],[],[],[],[]]
	
	# usar um counter ou adicionar tudo e depois remover os primeiros índices?
	c = 0
	for i in of:
		if c > 0:
			dados[0].append(i[0])
			dados[1].append(i[1])
			dados[2].append(i[2])
			dados[3].append(i[3])
			dados[4].append(i[4])
			dados[5].append(i[5])
			dados[6].append(i[6])
			dados[7].append(i[7])
			dados[8].append(i[8])
			dados[9].append(i[9])
			dados[10].append(i[10])
		c += 1

	df = pd.DataFrame({
		"nomes": dados[0],
		"email": dados[1],
		"whatsapp": dados[2],
		"RA": dados[3],
		"curso": dados[4],
		"período": dados[5],
		"campus": dados[6],
		"area": dados[7],
		"sub-área": dados[8],
		"qualidades": dados[9],
		"defeitos": dados[10]})
	df

with open("candidatos.csv", "r") as b:
	read(b)
