import matplotlib.pyplot as plt
import organizaemlistas
listaComdataevalores = organizaemlistas.dados.listaCOVID#todos os dados
doseUnica = organizaemlistas.totalu(listaComdataevalores) #lista com data e dados
#a funcao totalu chama a organizaçao dos dado sobre doses unicas aplicadas
v1dose = organizaemlistas.total1d(listaComdataevalores) #lista com data e dados
v2dose = organizaemlistas.total2d(listaComdataevalores) #lista com data e dados
totalv = organizaemlistas.totalvacinado(listaComdataevalores) #lista com data e dados

plt.plot(doseUnica[1],doseUnica[0])
plt.ylabel("doses unicas")
plt.show()

plt.plot(v1dose[1],v1dose[0])
plt.ylabel("1 doses ")
plt.show()

plt.plot(v2dose[1],v2dose[0])
plt.ylabel("2 doses")
plt.show()

plt.plot(totalv[1],totalv[0])
plt.ylabel("total")
plt.show()
