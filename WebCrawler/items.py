import scrapy


class ItemScraper(scrapy.Item):
    # The source URL:
    url_from = scrapy.Field()
    # The destination URL:
    url_to = scrapy.Field()
