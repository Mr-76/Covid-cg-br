# -*- coding: utf-8 -*-
import ast

with open ('covid.json','r',encoding="utf-8") as file: #import dos dados resultados do scraping
    a = file.readlines()

tamanho = len(a) #loop a lista
lista_contendoOsDicionarios = [] #criaço da lista nova com os dados organizados

for index in range(tamanho):
    if a[index] in ('][','[',']',']\n','][\n'): #evitando estes caracteres no loop
        continue
    try:# tentativa de transformar a string para dict
        #acaba evitando os caracteres acima tb caso nao sejam detectados
        transforma_paradict = ast.literal_eval(a[index])
    except SyntaxError:
        continue

    for key in transforma_paradict:
        lista_auxiliar = [] #para editar as strings
        for linha in transforma_paradict[key]:#limpando as linhas
            editar = linha
            linhaEditar = editar.replace('<h1 class="titulo-recebidas-aplicadas">','')
            linhaEditar = linhaEditar.replace('</h1>','')
            linhaEditar = linhaEditar.replace('<b>','')
            linhaEditar = linhaEditar.replace('</b>','')
            linhaEditar = linhaEditar.replace('<h2 class="valor-recebidas-aplicadas">','')
            linhaEditar = linhaEditar.replace('</h2>','')
            lista_auxiliar.append(linhaEditar)

        transforma_paradict[key] = [lista_auxiliar]#coletando os dados organizados
    lista_contendoOsDicionarios.append(transforma_paradict)
with open('dados.py','w',encoding="utf-8") as arquivo:#escrevendo os dados em py
    Dados = str(lista_contendoOsDicionarios)
    Dados = ('listaCOVID = '+Dados)
    arquivo.write(Dados)
