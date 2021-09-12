for i in b:

    c = i.replace('<h1 class="titulo-recebidas-aplicadas">','')
    c = c.replace('</h1>','')
    c = c.replace('<b>','')
    c = c.replace('</b>','')
    print(c)
