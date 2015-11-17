# -*- coding: utf-8 -*-
import scrapy


class MarketplaceSpider(scrapy.Spider):
    name = "marketplace"
    allowed_domains = ["marketplace.uchicago.edu"]
    start_urls = (
        'https://marketplace.uchicago.edu/',
    )

    def parse(self, response):
        pass
