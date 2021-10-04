import ast



with open ('covid.json','r') as file:
    a = file.readlines()


tamanho = len(a)

for index in range(tamanho):
    #print(a[index])
    if a[index] in ('][','[',']',']\n','][\n'):
        continue
    

    try:

        transforma_paradict = ast.literal_eval(a[index])

    except:
        continue

    for key in transforma_paradict:
        lista_auxiliar = []

        for linha in transforma_paradict[key]: 

            string = linha

            c = string.replace('<h1 class="titulo-recebidas-aplicadas">','')
            c = c.replace('</h1>','')
            c = c.replace('<b>','')
            c = c.replace('</b>','')
            c = c.replace('<h2 class="valor-recebidas-aplicadas">','')
            c = c.replace('</h2>','')
            
            lista_auxiliar.append(c)
#           print(c,'limpo')
        transforma_paradict[key] = [lista_auxiliar]

        print(transforma_paradict)
   



#for i in a:
 #   if a in ('][\n','[\n'):
  #      continue 
   # c = i.replace('<h1 class="titulo-recebidas-aplicadas">','')
   # c = c.replace('</h1>','')
   # c = c.replace('<b>','')
   # c = c.replace('</b>','')
   # print(c)
