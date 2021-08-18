# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from houtai.models import ershoufang
from houtai.models import newfang
from houtai.models import zufang


class SecondhouseItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = ershoufang
    pass

class NewhouseItem(DjangoItem):
    django_model = newfang
    pass

class ZuhouseItem(DjangoItem):
    django_model = zufang
    pass



