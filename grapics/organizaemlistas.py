#coding = utf-8
"""this code organizes some data"""
import dados

lista = dados.listaCOVID

def totalu(listatotal):
    """funcao organiza a bagunca que os dados estao orga
    ziados em 2 listas com respectivasdatas e valores.Ca
    is do que deixando simples.
    """
    listadata = []
    listavalores = []
    titulo="Total de does unicas"
    for i in listatotal:
        listavalores.append(i['value'][0][0])
        for key in i:
            if key != 'value':
                listadata.append(key)
    print(listadata,"\n",listavalores)
    return (listadata,listavalores,titulo)

def total1d(listatotal):
    """total de 1 doses"""
    listadata = []
    listavalores = []
    titulo = ("Total de 1 doses")
    for i in listatotal:
        listavalores.append(i['value'][0][1])
        for key in i:
            if key != 'value':
                listadata.append(key)
    print(listadata,"\n",listavalores)
    return (listadata,listavalores,titulo)
def total2d(listatotal):
    """total 2 doses"""
    listadata = []
    listavalores = []
    titulo = "Total de 2 doses"
    for i in listatotal:
        listavalores.append(i['value'][0][2])
        for key in i:
            if key != 'value':
                listadata.append(key)
    print(listadata,"\n",listavalores)
    return (listadata,listavalores,titulo)
def totalvacinado(listatotal):
    """total de vacinados"""
    listadata = []
    listavalores = []
    titulo="Percentual vacinado"
    for i in listatotal:
        listavalores.append(i['value'][0][3])
        for key in i:
            if key != 'value':
                listadata.append(key)
    print(listadata,"\n",listavalores)
    return (listadata,listavalores,titulo)
totalu(lista)
total1d(lista)
total2d(lista)
totalvacinado(lista)
