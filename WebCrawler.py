import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import requests

class WebCrawler(scrapy.Spider):
    name = 'simple_crawler'
    start_urls = ['http://example.com']

    def parse(self, response):
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        # Extract text from the page
        text = soup.get_text()
        url = response.url

        # Save the page content (store the data somewhere)
        with open('crawled_data.txt', 'a') as f:
            f.write(f'URL: {url}\n')
            f.write(text)
            f.write('\n' + '=' * 40 + '\n')

        # Follow links to new pages (get all anchor tags)
        for link in soup.find_all('a', href=True):
            yield response.follow(link['href'], self.parse)

# Start the crawler
process = CrawlerProcess()
process.crawl(WebCrawler)
process.start()
