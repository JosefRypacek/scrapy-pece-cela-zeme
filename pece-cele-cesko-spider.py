#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Kod je hodne uzpusobeny moznosti nasledneho tisku ziskane "kucharky".
# Napriklad je pouzita fixni html width a height pro kazdy obrazek, aby bylo mozne
# zkopirovat cely vysledek z Google Chrome do LibreOffice Writer a zachovat pomery stran.
#

import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.ceskatelevize.cz/porady/12309875102-pece-cela-zeme/12530-recepty/']
    custom_settings = {
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1
    }
    html_file = open('output.html', 'w')

    # z hlavni stranky najdi vsechny recepty a zpracuje je
    def parse(self, response):
        self.html_file.write('<link rel="stylesheet" href="style.css" />')

        i = 1000;
        for recept in response.css('div.minibox'):
            recept_url = recept.css('a ::attr(href)').get()
            recept_url = response.urljoin(recept_url)
            img = recept.css('img')
            img_url = img.css('::attr(src)').get()
            img_width = img.css('::attr(width)').get()
            img_height = img.css('::attr(height)').get()

            request = scrapy.Request(recept_url, callback=self.parse_recept, priority=i)
            request.cb_kwargs['img_url'] = response.urljoin(img_url).replace('/m_', '/')
            request.cb_kwargs['img_width'] = img_width
            request.cb_kwargs['img_height'] = img_height
            yield request
            i = i-1

    # vlastni zpracovani kazdeho receptu
    def parse_recept(self, response, img_url, img_width, img_height):
        autor = response.css('div.explanatory-text.obsah.kontext h6 ::text').get().strip();
        nazev = response.css('div.recept.obsah h3 ::text').get();
        text = response.css('div.recept.obsah:nth-child(2)').get();
        fotky = response.css('section.gallery_v2')

        output = '<div class="receptbox"><h2>' + nazev + ' (' + autor + ')</h2>' + '<img class="imgmain" width="' + img_width + '" height="' + img_height + '" src="' + img_url + '">' + text
        self.html_file.write(output)

        self.html_file.write('<div class="imgbox">')
        for f in fotky.css('a'):
            size = f.css('::attr(data-size)').get()
            width = int(size.split('x')[0])
            height = int(size.split('x')[1])
            scale = width / 210
            url = response.urljoin(f.css('::attr(href)').get())
            f = '<img class="imgadd" width="' + str(width / scale) + '" height="' + str(height / scale) + '" src="' + url + '">'
            self.html_file.write(f)

        self.html_file.write('</div></div>')
