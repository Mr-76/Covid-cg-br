import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


def cria_dict(data,lista_texto_valores,lista_valores):
    dicionario_para_json = {"Data": data}
    for i, item in enumerate(lista_texto_valores):
        dicionario_para_json[item.text] = lista_valores[i]
    return dicionario_para_json

def load_dados_json(nome_file,dicionario_web): 
    with open(nome_file,'r') as file:
        lista_dict_total = json.load(file)
    lista_dict_total.append(dicionario_web)    
    escreve_lista_js(lista_dict_total,nome_file)


def escreve_lista_js(lista_dicionario,nome):
    with open(nome,'w',encoding = "utf-8") as file:
            json.dump(lista_dicionario,file,ensure_ascii=False,indent=1)




nome_file = "dados.json"
DATA_TODAY = datetime.now() 
DATA_TODAY = ("{}/{}/{}").format(DATA_TODAY.day,DATA_TODAY.month,DATA_TODAY.year)
parser = 'html.parser'
pagina_web = requests.get('https://campinagrande.pb.gov.br/')
pagina_soup = BeautifulSoup(pagina_web.text,parser)
lista_texto_web = pagina_soup.find_all("p",class_="title")
lista_valores_web = pagina_soup.find_all("p",class_="count")
for index in range(len(lista_texto_web)):
    string_to_int = str(lista_valores_web[index].text.replace("%",""))
    lista_valores_web[index] = int(string_to_int)


dicionario_json = cria_dict(DATA_TODAY,lista_texto_web,lista_valores_web)
load_dados_json(nome_file,dicionario_json)
