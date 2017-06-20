# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SampleScraperItem(scrapy.Item):
    """
    A default track on beatports.com
    """
    active = scrapy.Field()
    artists = scrapy.Field()
    audio_format = scrapy.Field()
    bpm = scrapy.Field()
    component = scrapy.Field()
    component_type = scrapy.Field()
    date = scrapy.Field()
    duration = scrapy.Field()
    exclusive = scrapy.Field()
    formats = scrapy.Field()
    genres = scrapy.Field()
    guest_pick = scrapy.Field()
    id = scrapy.Field()
    images = scrapy.Field()
    key = scrapy.Field()
    label = scrapy.Field()
    mix = scrapy.Field()
    name = scrapy.Field()
    preorder = scrapy.Field()
    preview = scrapy.Field()
    price = scrapy.Field()
    purchase = scrapy.Field()
    purchase_type = scrapy.Field()
    release = scrapy.Field()
    remixers = scrapy.Field()
    sale_type = scrapy.Field()
    slug = scrapy.Field()
    sponsored = scrapy.Field()
    sub_genres = scrapy.Field()
    title = scrapy.Field()
    type = scrapy.Field()
    waveform = scrapy.Field()

