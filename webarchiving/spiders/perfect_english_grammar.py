# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PerfectEnglishGrammarSpider(CrawlSpider):
    name = "perfect-english-grammar"
    allowed_domains = ["perfect-english-grammar.com"]
    start_urls = (
        'http://www.perfect-english-grammar.com/',
    )

    rules = [
        Rule(LinkExtractor(allow=['.*']), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        print response.url
        with open('output.log', 'a') as f:
            f.write(response.url)
            f.write('\n')
