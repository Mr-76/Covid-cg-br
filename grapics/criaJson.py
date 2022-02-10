import json
import organizaemlistas

def corrige_string(lista_data):
    for index_data in range(len(lista_data)):    
        int_list = []
        string = lista_data[index_data].split("/")
        for index_split in range(len(string)):
            to_int = int(string[index_split])
            int_list.append(to_int)
        lista_data[index_data] = ("{}/{}/{}".format(int_list[0]
                                            ,int_list[1]
                                            ,int_list[2]))



DADOS = organizaemlistas.dados.listaCOVID
listaComdataevalores = organizaemlistas.dados.listaCOVID#todos os dados
doseUnica = organizaemlistas.totalu(listaComdataevalores) #lista com data e dados
v1dose = organizaemlistas.total1d(listaComdataevalores) #lista com data e dados
v2dose = organizaemlistas.total2d(listaComdataevalores) #lista com data e dados
totalv = organizaemlistas.totalvacinado(listaComdataevalores) #lista com data e dados


data = v1dose[0]
corrige_string(data)

doseUnica = organizaemlistas.totalu(listaComdataevalores)[1]
dose1d = organizaemlistas.total1d(listaComdataevalores)[1]
dose2d = organizaemlistas.total2d(listaComdataevalores)[1]
TotalV = organizaemlistas.totalvacinado(listaComdataevalores)[1]

listaJson = []

for i in range(len(data)):
    dicionario = {}
    dicionario["Data"] = data[i]
    dicionario["Doses Unicas"] = int(doseUnica[i])
    dicionario["Dose 1"] = int(dose1d[i])
    dicionario["Dose 2"] = int(dose2d[i])
    dicionario["Total percentagem"] = int(TotalV[i].replace("%",""))
    listaJson.append(dicionario)

with open('dados.json', 'w', encoding='utf-8') as file:
        json.dump(listaJson, file, ensure_ascii=False, indent=1)
