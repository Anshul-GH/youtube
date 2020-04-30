# -*- coding: utf-8 -*-
import scrapy
# add a reference to the items class
from ..items import MyscrapperItem

# observe that the items class is a level up in directory hierarcy 
# hence the reference needs a .. notation



class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    # allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # the getall() function fetches all the values together
        authorName=response.css("small.author::text").getall()
        quotes=response.css("span.text::text").getall()

        # lets print the values on the console
        # print(authorName)
        # print(quotes)

        # create an object of the items class
        obj = MyscrapperItem()
        obj['aname'] = authorName
        obj['quote'] = quotes

        # instead of default 'pass' we need to return the object
        # of the items class

        return obj
        
