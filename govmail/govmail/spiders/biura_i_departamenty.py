# -*- coding: utf-8 -*-
import scrapy
import re

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
            nazwa_ministerstwa = ministestwo.xpath('.//text()').get().replace('\n', ' ')
            # link to the website
            href = 'https://www.gov.pl'+ministestwo.xpath('.//@href').get()
            # #add to every scaraped url
            biura_i_departamenty = '/biura-i-departamenty-1'


            href += biura_i_departamenty

            #follow to page
            yield response.follow(url = href, callback = self.parse_biura_i_departamenty,
                                   meta={'nazwa':nazwa_ministerstwa, 'href':href},
                                   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})

    def parse_biura_i_departamenty(self, response):
        #copying meta
        nazwa_ministerstwa = response.request.meta['nazwa']
        href = response.request.meta['href']

        #scraping all biura i departenty
        biura = response.xpath('//*[@id="body"]/main/div/article/div[1]/ul/li/a')
        for biuro in biura:
            nazwa_biura = biuro.xpath('.//div/div/text()').get()
            deep_href = 'https://www.gov.pl'+biuro.xpath('.//@href').get()


            #follow to page
            yield response.follow(url = deep_href, callback = self.parse_email_i_kontaktowe,
                                   meta={'nazwa_ministerstwa':nazwa_ministerstwa,'nazwa_biura':nazwa_biura,'deep_href':deep_href},
                                   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})

        next_page = response.xpath('//*[@id="js-pagination-page-next"]/@href').get()
        if next_page:
            yield scrapy.Request(url = href+next_page, callback=self.parse_biura_i_departamenty,meta = {'nazwa':nazwa_ministerstwa, 'href':href}, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})


    def parse_email_i_kontaktowe(self, response):
        #copying meta
        nazwa_ministerstwa = response.request.meta['nazwa_ministerstwa']
        nazwa_biura = response.request.meta['nazwa_biura']
        deep_href = response.request.meta['deep_href']

        html_text = str(response.text)
        #set delets dulicates!
        mail_list = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', html_text)
        mail_list = list(filter(lambda email: len(email) < 60, mail_list))

        yield {
            "Ministerstwo" : nazwa_ministerstwa,
            "Nazwa biura/departamentu" : nazwa_biura,
            "Link to biura" : deep_href,
            "Znalezione maile": str(set(mail_list)),
        }
