# -*- coding: utf-8 -*-
import scrapy
from ..items import MyfirstscrapyprojectItem

class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    # allowed_domains = ['http://http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        aname = response.css("small.author::text").getall()
        quotes = response.css("span.text::text").getall()

        obj = MyfirstscrapyprojectItem()
        obj['name']=aname
        obj['qot']=quotes
        
        yield obj
