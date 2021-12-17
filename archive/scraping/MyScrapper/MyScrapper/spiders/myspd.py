# -*- coding: utf-8 -*-
import scrapy
# note that items class is a directory level above hence the .. notation
from ..items import MyscrapperItem


class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    
    def parse(self, response):
        authorNames=response.css("small.author::text").getall()
        quotes=response.css("span.text::text").getall()

        # lets print these values and check
        # print(authorNames)
        # print(quotes)

        # lets create a new object of the items class
        obj = MyscrapperItem()
        obj['aname']=authorNames
        obj['quote']=quotes

        # instead of pass we will have to return the object now
        return obj
