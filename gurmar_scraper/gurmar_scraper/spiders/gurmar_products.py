# gtin_project/gtin_project/spiders/gtin_spider.py

import scrapy
#Sayfaları gezmeyen kod
"""class GTINSpider(scrapy.Spider):
    name = 'gtin'
    allowed_domains = ['gurmar.com.tr']
    start_urls = ['https://www.gurmar.com.tr/at%C4%B1stirmaliklar']

    def parse(self, response):
        # Extracting the URLs of the product detail pages
        product_urls = response.css('.product-item .details a::attr(href)').getall()
        for url in product_urls:
            yield response.follow(url, self.parse_product)

    def parse_product(self, response):
        # Extract product details like name and price, as you have done or will do in your code
        product_name = response.css('.product-name h1::text').get()
        product_price = response.css('div.product-price span.price::text').get()

        # Extract the GTIN number using the div class and the span class
        gtin = response.css('div.gtin span.value::text').get()

        yield {
            'name': product_name.strip() if product_name else None,
            'price': product_price.strip() if product_price else None,
            'gtin': gtin.strip() if gtin else None,  # Ensure to strip the result to remove any surrounding whitespace
            'url': response.url
        }

"""
#Sayfa sayfa gezen hali
import scrapy

class GTINSpider(scrapy.Spider):
    name = 'gtin'
    allowed_domains = ['gurmar.com.tr']
    start_urls = ['https://www.gurmar.com.tr/at%C4%B1stirmaliklar']

    def parse(self, response):
        # Extracting the URLs of the product detail pages
        product_urls = response.css('.product-item .details a::attr(href)').getall()
        for url in product_urls:
            yield response.follow(url, self.parse_product)

        # Construct the URL for the next page
        current_page_number = response.url.split('pagenumber=')[-1] if 'pagenumber=' in response.url else 1
        next_page_number = int(current_page_number) + 1
        next_page_url = f"https://www.gurmar.com.tr/at%C4%B1stirmaliklar?pagenumber={next_page_number}"

        # Check if there are products on the next page by checking if any product URLs were extracted
        while(next_page_number < 6):
            if product_urls:
                yield response.follow(next_page_url, self.parse)
            next_page_number += 1
        

    def parse_product(self, response):
        # Extract product details like name and price, as you have done or will do in your code
        product_name = response.css('.product-name h1::text').get()
        product_price = response.css('div.product-price span.price::text').get()

        # Extract the GTIN number using the div class and the span class
        gtin = response.css('div.gtin span.value::text').get()

        yield {
            'name': product_name.strip() if product_name else None,
            'price': product_price.strip() if product_price else None,
            'gtin': gtin.strip() if gtin else None,
            'url': response.url
        }
