# -*- coding: utf-8 -*-
import scrapy
from scrapy_grandFantasia.items import NavigationItem


class NavigationSpider(scrapy.Spider):
    name = 'Navigation'
    allowed_domains = ['pt.grandfantasia.info']
    start_urls = ['http://pt.grandfantasia.info/']

    def parse(self, response):
        for item in response.css("li"):
            title = item.css("span::text").extract_first()
            ##
            if title is not None:
               navigation = NavigationItem(title=title)
               yield navigation
