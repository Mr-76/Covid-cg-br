import scrapy
from datetime import datetime
data_hj = datetime.now()

data_hj = ("0{}/0{}/{}").format(data_hj.day,data_hj.month,data_hj.year)
print(data_hj,"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

#data_hj_config = data_hj.strftime(‘%d/%m/%Y’)
class CovidSpider(scrapy.Spider):
    name = "covid"
    start_urls = [
        'https://campinagrande.pb.gov.br/coronavirus/'
    ]

    def parse(self, response):
        for linha in response.css('html'):
            print('PRINTANDO OOOOOOO')
            print(linha.css('.titulo-recebidas-aplicadas').getall())
            
            yield {
                    data_hj: linha.css('.titulo-recebidas-aplicadas').getall(),'value':linha.css('.valor-recebidas-aplicadas').getall()
            }
#.replace('<h1 class="titulo-recebidas-aplicadas">','').replace('/b','').replace('<','').replace('b>','').replace('>','').replace('/h1',''),
#limpa dados
#criat funçaoi
#c
