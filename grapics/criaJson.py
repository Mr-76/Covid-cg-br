import json
import organizaemlistas

DADOS = organizaemlistas.dados.listaCOVID
listaComdataevalores = organizaemlistas.dados.listaCOVID#todos os dados
doseUnica = organizaemlistas.totalu(listaComdataevalores) #lista com data e dados
v1dose = organizaemlistas.total1d(listaComdataevalores) #lista com data e dados
v2dose = organizaemlistas.total2d(listaComdataevalores) #lista com data e dados
totalv = organizaemlistas.totalvacinado(listaComdataevalores) #lista com data e dados


data = v1dose[0]
doseUnica = organizaemlistas.totalu(listaComdataevalores)[1]
dose1d = organizaemlistas.total1d(listaComdataevalores)[1]
dose2d = organizaemlistas.total2d(listaComdataevalores)[1]
TotalV = organizaemlistas.totalvacinado(listaComdataevalores)[1]

listaJson = []

for i in range(25):
    dicionario = {}
    dicionario["Data"] = data[i]
    dicionario["Doses Unicas"] = int(doseUnica[i])
    dicionario["Dose 1"] = int(dose1d[i])
    dicionario["Dose 2"] = int(dose2d[i])
    dicionario["Total percentagem"] = int(TotalV[i].replace("%",""))
    listaJson.append(dicionario)

with open('datos.json', 'w', encoding='utf-8') as file:
        json.dump(listaJson, file, ensure_ascii=False, indent=1)
