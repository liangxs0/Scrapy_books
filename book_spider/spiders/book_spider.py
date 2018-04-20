import scrapy

class BooksSpider(scrapy.Spider):
    #定义一个爬虫
    name = "books"
    #定义爬虫的起点
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        #提取数据
        #获取每一本书的信息都在标签 class=“b-all-content cf”
        #利用CSS的方法找到所有的元素，并一次迭代
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {'name':name,
                    'price':price,
                   }

            #提取链接
            next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
            if next_url:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url,callback=self.parse)

