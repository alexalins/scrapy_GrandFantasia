# -*- coding: utf-8 -*-
import scrapy


class MineracaoSpider(scrapy.Spider):
    name = 'Mineracao'
    allowed_domains = ['https://pt.grandfantasia.info/items/23--24--1--mining/']
    start_urls = ['https://pt.grandfantasia.info/items/23--24--1--mining/']

    def parse(self, response):
        for item in response.css('div.item-description'):
            title = item.css('div h3 a::attr(title)').extract_first()
            image = item.css('div div img::attr(src)').extract_first()
            if title is not None:
                title = title.replace("view ", "")
                yield {'title': title, 'image': image}

