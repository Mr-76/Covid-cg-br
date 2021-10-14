#programar orgazina os dados em listas de acordo com os seus titulos
import dados
lista = dados.listaCOVID

listadata = []
listavalores = []

def totalu(lista):
"""
funcao organiza a bagunca que os dados estao orgaziados em 2 listas com respectivasdatas e valores. Cada funcao faz a mesma coisa so muda o titulo que por sinal
fiz um scrap bem porco e acabei atrapalhando mais do que deixando simple
"""
    listadata = []
    listavalores = []
    TITULO = "Total de does unicas"    
    for i in lista:
        listavalores.append(i['value'][0][0])
        for b in i:
            if b != 'value':
                    listadata.append(b)
    print(listadata,"\n",listavalores)

def total1d(lista):
    listadata = []
    listavalores = []
    TITULO = "Total de 1 doses"    
    for i in lista:
        listavalores.append(i['value'][0][1])
        for b in i:
            if b != 'value':
                    listadata.append(b)
    print(listadata,"\n",listavalores)


def total2d(lista):
    listadata = []
    listavalores = []
    TITULO = "Total de 2 doses"    
    for i in lista:
        listavalores.append(i['value'][0][2])
        for b in i:
            if b != 'value':
                    listadata.append(b)
    print(listadata,"\n",listavalores)


def totalvacinado(lista):
    listadata = []
    listavalores = []
    TITULO = "Percentual vacinado"    
    for i in lista:
        listavalores.append(i['value'][0][3])
        for b in i:
            if b != 'value':
                    listadata.append(b)
    print(listadata,"\n",listavalores)


totalu(lista)
total1d(lista)
total2d(lista)
totalvacinado(lista)




