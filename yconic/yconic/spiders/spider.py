# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['yconic.com']
    start_urls = ['https://yconic.com/feed/most-recent/%d/50' %n for n in range(0, 200, 50)]

    def parse(self, response):
        posts = response.xpath('//div[@class="feed_item--thread js-feed_item-thread js-impression_marker"]')
        for post in posts:
            title = post.xpath('./a[@class="title js-link_followed_marker"]/text()').extract_first().strip()
            description = post.xpath('./div[@class="feed_item--thread__content js-community-content"]/text()').extract_first().strip()
            topics = post.xpath('./ul/li[@class="horizontal_list--item"]/a/text()').extract()

            fields = dict(title=title, description=description, topics=topics)
            yield fields
