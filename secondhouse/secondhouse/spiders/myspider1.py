import scrapy
from secondhouse.items import NewhouseItem

class Myspider1Spider(scrapy.Spider):
    name = 'myspider1'
    #allowed_domains = ['wh.lianjia.com']
    urls = 'https://wh.fang.lianjia.com/loupan/pg{}'
    page = 1
    start_urls = [urls.format(str(page))]

    def parse(self, response):
        all_data = response.xpath("//div[@class='resblock-desc-wrapper']")
        for i in all_data:
            house1 = NewhouseItem()
            house1["name"] = i.xpath("div[@class='resblock-name']/a/text()").extract()[0]
            house1["position1"] =i.xpath("div[@class='resblock-location']/span[1]/text()").extract()[0]
            house1["position2"] = i.xpath("div[@class='resblock-location']/span[2]/text()").extract()[0]
            house1["position3"] = i.xpath("div[@class='resblock-location']/a/text()").extract()[0]
            if i.xpath("div[@class='resblock-area']/span[1]/text()").extract():
                house1["houseinfo"] = i.xpath("div[@class='resblock-area']/span[1]/text()").extract()[0]
            else:
                house1["houseinfo"] ="暂无房屋信息"

            if i.xpath("div[@class='resblock-price']/div[@class='main-price']/span[1]/text()").extract()[0]:
                house1["unitPrice"] = i.xpath("div[@class='resblock-price']/div[@class='main-price']/span[1]/text()").extract()[0]
            else:
                house1["unitPrice"] = "暂未定价"

            if i.xpath("div[@class='resblock-price']/div[@class='main-price']/span[1]/text()").extract()[0]!="价格待定":
                house1["totalPrice"] = i.xpath("div[@class='resblock-price']/div[@class='second']/text()").extract()[0]
            else:
                house1["totalPrice"] = "暂无价格"

            yield house1

        # 获取下一页的网页、路径
        self.page += 1
        next_urls = self.urls.format(str(self.page))
        if self.page < 101:
            yield scrapy.Request(url=next_urls, callback=self.parse)


