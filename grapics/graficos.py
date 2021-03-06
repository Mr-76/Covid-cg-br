import matplotlib.pyplot as plt

import organizaemlistas

listaComdataevalores = organizaemlistas.dados.listaCOVID#todos os dados
doseUnica = organizaemlistas.totalu(listaComdataevalores) #lista com data e dados
#a funcao totalu chama a organizaçao dos dado sobre doses unicas aplicadas
v1dose = organizaemlistas.total1d(listaComdataevalores) #lista com data e dados
v2dose = organizaemlistas.total2d(listaComdataevalores) #lista com data e dados
totalv = organizaemlistas.totalvacinado(listaComdataevalores) #lista com data e dados

plt.plot(doseUnica[0],doseUnica[1])
plt.ylabel("doses unicas")
plt.show()

plt.plot(v1dose[0],v1dose[1])
plt.ylabel("1 doses ")
plt.show()

plt.plot(v2dose[0],v2dose[1])
plt.ylabel("2 doses")
plt.show()

plt.plot(totalv[0],totalv[1])
plt.ylabel("total")
plt.show()

print("dosees unicas")
print(doseUnica[1])
print("\n")


def media_por_data(titulo,dado,ponto0,ponto1):
    """
    titulo é o nome dos dados que vc esta usando
    dado é lista com os valores
    ponto0 e ponto 1 sao as datas
    por fim a funtaçao retorna a media no periodo de tempo especificado
    """
    print("---------",titulo,"---------")
    dados_data= dado[0]
    dados_valores = dado[1]
    ponto0 = dados_data.index(ponto0)
    ponto1 = (dados_data.index(ponto1)) + 1 #chamar ex de 05/06/2021 a
                                           # 06/06/2021 inde de 05 é 0
                                           # index de 06 é 1 se coloar
                                           # no range roda so 1 vez for in in range(0,1),
                                           # tb ja #ex: de 05/06/2021 ate 07/06/21 ,
                                           # 05 tem index 0 e 07 tem index 2 2 - 0 = 2 +1 < ----
                                           # para fazer a media
    soma = 0
    divisor = (ponto1 - ponto0)

    for marcador in range(ponto0,ponto1):
        dados_valores[marcador] = (dados_valores[marcador]).replace("%","")
        soma += float(dados_valores[marcador])
    media_dt = soma/divisor
    return media_dt


media = media_por_data("doses unicas",doseUnica,'06/09/2021','011/01/2022')
print(media)
media = media_por_data("1 doses",v1dose,'06/09/2021','011/01/2022')
print(media)
media = media_por_data("2 dose ",v2dose,'06/09/2021','011/01/2022')
print(media)
media = media_por_data("total em % ",totalv,'06/09/2021','011/01/2022')


print(media)
