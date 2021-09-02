import scrapy


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
                'text': linha.css('.titulo-recebidas-aplicadas').getall(),
                'values':linha.css('.valor-recebidas-aplicadas').getall()
            }

