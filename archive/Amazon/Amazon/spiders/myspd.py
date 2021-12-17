# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    # allowed_domains = ['https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_85%3A10440599031&s=price-asc-rank&dc&qid=1588323876&rnid=1389432031&ref=sr_nr_n_2']
    start_urls = ['https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_85%3A10440599031&s=price-asc-rank&dc&qid=1588323876&rnid=1389432031&ref=sr_nr_n_2']

    def parse(self, response):
        mobNames = response.css('span.a-text-normal::text').getall()
        mobPrices = response.css('span.a-price-whole::text').getall()

        obj = AmazonItem()
        obj['mobName'] = mobNames
        obj['mobPrice'] = mobPrices

        return obj
