import scrapy
from secondhouse.items import SecondhouseItem
import time

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    #allowed_domains = ['wh.lianjia.com']
    page = 1
    start_urls = ['http://wh.lianjia.com/ershoufang/pg1']

    def parse(self, response):
        # 匹配所有的li标签
        all_data = response.xpath("//ul[@class='sellListContent']/li")
        # 遍历每一条li标签
        for i in all_data:
            house = SecondhouseItem()
            house["title"] = i.xpath("div[@class='info clear']/div[@class='title']/a/text()").extract()[0]
            house["img"] = i.xpath("a/img[2]/@data-original").extract()[0]
            house["position1"] = i.xpath("div[@class='info clear']/div[@class='flood']/div[@class='positionInfo']/a[1]/text()").extract()[0]
            house["position2"] = i.xpath("div[@class='info clear']/div[@class='flood']/div[@class='positionInfo']/a[2]/text()").extract()[0]
            if i.xpath("div[@class='info clear']/div[@class='address']/div[@class='houseInfo']/text()").extract()[0]:
                houseinfo = i.xpath("div[@class='info clear']/div[@class='address']/div[@class='houseInfo']/text()").extract()[0]
                house["houseInfo1"] = houseinfo.split('|')[0]
                house["houseInfo2"] = houseinfo.split('|')[1]
                house["houseInfo3"] = houseinfo.split('|')[2]
            else:
                house["houseInfo1"] = "暂无详细信息"
                house["houseInfo2"] = "暂无详细信息"
                house["houseInfo3"] = "暂无详细信息"
            house["totalPrice"] = i.xpath("div[@class='info clear']/div[@class='priceInfo']/div[@class='totalPrice']/span/text()").extract()[0]
            if i.xpath("div[@class='info clear']/div[@class='priceInfo']/div[@class='unitPrice']/span/text()").extract()[0]:
                house["unitPrice"] = i.xpath("div[@class='info clear']/div[@class='priceInfo']/div[@class='unitPrice']/span/text()").extract()[0]
            else:
                house["unitPrice"] = "暂无详细信息"
            pos_url = i.xpath("div[@class='info clear']/div[@class='title']/a/@href").extract()[0]  # daqulujing
            yield scrapy.Request(url=pos_url, callback=self.parse_detail, meta={'house': house})

        # 获取下一页的网页、路径
        time.sleep(5)
        self.page = self.page + 1
        if self.page < 101:
            next_urls = 'http://wh.lianjia.com/ershoufang/pg' + str(self.page)
            yield scrapy.Request(url=next_urls, callback=self.parse)


    # 函数声明:二级爬虫
    def parse_detail(self, response):
        house = response.meta['house']
        # 二级页面数据
        all_data1 = response.xpath("//div[@class='areaName']")
        for j in all_data1:
            house["position3"] = j.xpath("span[2]/a[1]/text()").extract()[0]
            yield house