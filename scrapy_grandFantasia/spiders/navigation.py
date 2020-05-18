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
            children = []
            for child in item.css("ul li"):
                titleChild = child.css("li a::text").extract_first()
                if titleChild is not None:
                    children.append(titleChild)
            ##
            if title is not None:
               navigation = NavigationItem(title=title, children=children)
               yield navigation
