# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YeastractItem(scrapy.Item):

    proteinname = scrapy.Field()
    description = scrapy.Field()
    go_BioProc = scrapy.Field()
    go_MolFunc = scrapy.Field()
    go_CellComp = scrapy.Field()
