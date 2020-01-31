"""sources: https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/
https://docs.scrapy.org/en/latest/topics/settings.html
https://docs.scrapy.org/en/latest/faq.html#faq-bfo-dfo
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.downloadermiddlewares import robotstxt
from scrapy.linkextractors import LinkExtractor
from scrapy.pqueues import DownloaderAwarePriorityQueue
from scrapy.settings.default_settings import SCHEDULER_PRIORITY_QUEUE, DEPTH_PRIORITY, \
    SCHEDULER_DISK_QUEUE, SCHEDULER_MEMORY_QUEUE, CLOSESPIDER_ITEMCOUNT, COOKIES_ENABLED, CONCURRENT_REQUESTS
from scrapy.spiders import CrawlSpider, Rule
from scrapy.squeues import PickleFifoDiskQueue, FifoMemoryQueue

from items import ItemScraper


class WikiScraper(CrawlSpider):
    # The name of the spider is:
    name = "wiki"

    # Allowed domains:
    allowed_domains = ["wikipedia.org"]

    # The URL to start with:
    start_urls = ["https://en.wikipedia.org/wiki/Scooby-Doo"]

    custom_settings = {
        robotstxt: True,
        SCHEDULER_PRIORITY_QUEUE: DownloaderAwarePriorityQueue,
        DEPTH_PRIORITY: 1,
        SCHEDULER_DISK_QUEUE: PickleFifoDiskQueue,
        SCHEDULER_MEMORY_QUEUE: FifoMemoryQueue,
        CLOSESPIDER_ITEMCOUNT: 1,
        COOKIES_ENABLED: False,
        CONCURRENT_REQUESTS: 100,
    }

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'results.csv'
    })

    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=False,
            callback="parse_items"
        )
    ]

    # Begin visiting all original start URLS
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self, response):
        # All found links:
        items = []
        # Only pull unique links
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            is_allowed = True
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If link is allowed create a new item and add it to the list
            if is_allowed:
                item = ItemScraper()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        # Return all found and allowed items
        return items
