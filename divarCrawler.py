

import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote-spdier'
    start_urls = ['https://quotes.toscrape.com']