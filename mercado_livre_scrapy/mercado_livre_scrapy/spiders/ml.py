import scrapy

class MlSpider(scrapy.Spider):
    name = 'ml'
    # Vamos fazer requisicoes de todos esses links através de list comprehension
    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page={i}' for i in range(1, 210)]

    def parse(self, response, **kwargs):
        # // Consulta inicia na raiz do documento * Busca tudo
        for i in response.xpath('//*[@class="promotion-item"]'):  # Caminho com sintaxe xpath para nó class="promotion"
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()  # Pega todos os itens em forma de lista
            title = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            link = i.xpath('./a/@href').get()

            #  Retorna um generator
            yield {
                'price': price,
                'title': title,
                'link': link
            }
