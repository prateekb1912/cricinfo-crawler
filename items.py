# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CricinfoCrawlerItem(scrapy.Item):
    team1 = scrapy.Field()
    team2 = scrapy.Field()
    winner = scrapy.Field()
    margin = scrapy.Field()
    venue = scrapy.Field()
    match_date = scrapy.Field()
    match_no = scrapy.Field()
