# -*- coding: utf-8 -*-
import scrapy


class BiuraIDepartamentySpider(scrapy.Spider):
    name = 'biura_i_departamenty'
    allowed_domains = ['www.gov.pl']
    start_urls = ['https://www.gov.pl/web/gov/ministerstwa']

    # basic spoofing
    def start_requests(self):
        yield scrapy.Request(url = 'https://www.gov.pl/web/gov/ministerstwa',
                              callback=self.parse,
                              headers= { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})

    # using for collecting all ministerstwa from page
    def parse(self, response):
        ministerstwa = response.xpath('//*[@id="body"]/main/section/section/ul/li/h3/a')
        for ministestwo in ministerstwa:
            nazwa = ministestwo.xpath('.//text()').get().replace('\n', ' ')
            # link to the website
            href = 'https://www.gov.pl'+ministestwo.xpath('.//@href').get()
            # #add to every scaraped url
            biura_i_departamenty = '/biura-i-departamenty'
            href += biura_i_departamenty

            #follow to page


    def parse_biura_i_departamenty(self, response):
        pass

    def parse_email_i_kontaktowe(self, response):
        pass
