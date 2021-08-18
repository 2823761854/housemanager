import scrapy
from secondhouse.items import ZuhouseItem

# scrapy crawl myspider2

class Myspider2Spider(scrapy.Spider):
    name = 'myspider2'
    #allowed_domains = ['wh.lianjia.com']
    urls = 'http://wh.lianjia.com/zufang/pg{}'
    page = 1
    start_urls = [urls.format(str(page))]

    def parse(self, response):
        all_data = response.xpath("//div[@class='content__list--item--main']")
        for i in all_data:
            house2 = ZuhouseItem()
            if i.xpath("p[@class='content__list--item--title']/a/text()").extract()[0]:
                house2["title"] = i.xpath("p[@class='content__list--item--title']/a/text()").extract()[0]
            else:
                house2["title"] ="暂无信息"
            house2["position1"] = i.xpath("p[@class='content__list--item--des']/a[1]/text()").extract()[0]
            house2["position2"] = i.xpath("p[@class='content__list--item--des']/a[2]/text()").extract()[0]
            house2["position3"] = i.xpath("p[@class='content__list--item--des']/a[3]/text()").extract()[0]
            house2["totalPrice"] = i.xpath("span/em/text()").extract()[0]
            if i.xpath("p[@class='content__list--item--des']/text()[1]").extract()[0] == '\n                  精选          ':
                house2["size_room"] = i.xpath("p[@class='content__list--item--des']/text()[6]").extract()[0]
                house2["area_room"] = i.xpath("p[@class='content__list--item--des']/text()[7]").extract()[0]
                house2["num_room"] = i.xpath("p[@class='content__list--item--des']/text()[8]").extract()[0]
            else:
                house2["size_room"] = i.xpath("p[@class='content__list--item--des']/text()[5]").extract()[0]
                house2["area_room"] = i.xpath("p[@class='content__list--item--des']/text()[6]").extract()[0]
                house2["num_room"] = i.xpath("p[@class='content__list--item--des']/text()[7]").extract()[0]
            yield house2

        # 获取下一页的网页、路径
        self.page += 1
        next_urls = self.urls.format(str(self.page))
        if self.page < 101:
            yield scrapy.Request(url=next_urls, callback=self.parse)
