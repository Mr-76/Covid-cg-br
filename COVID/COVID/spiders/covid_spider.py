from datetime import datetime
import scrapy
DATA_HJ = datetime.now()

DATA_HJ = ("0{}/0{}/{}").format(DATA_HJ.day,DATA_HJ.month,DATA_HJ.year)
print(DATA_HJ,"Data")


class CovidSpider(scrapy.Spider):
    """Spider que faz o scraping do covid """
    name = "covid"
    start_urls = [
        'https://campinagrande.pb.gov.br/coronavirus/'
    ]

    def parse(self, response):
        for linha in response.css('html'):
            print('PRINTANDO OOOOOOO')
            print(linha.css('.titulo-recebidas-aplicadas').getall())

            yield {
            DATA_HJ: linha.css('.titulo-recebidas-aplicadas').getall(),
            'value':linha.css('.valor-recebidas-aplicadas').getall()
            }
