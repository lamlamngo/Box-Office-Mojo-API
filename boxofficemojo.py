from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from bs4 import BeautifulSoup

class BoxOfficeMojo(object):

    YEAR_START = 1982
    WEEKEND_URLS = "https://www.boxofficemojo.com/weekend/?yr=!!!!&sort=year&order=DESC&p=.htm" 
    BASE_URL = "https://www.boxofficemojo.com"

    def __init__(self):
        self.year_weekend_url = {}
        self.crawl_for_weekend_urls()
    
    def get_proxies(self):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

    def crawl_for_weekend_urls(self):
        for year in range(1982,2019):
            url = self.WEEKEND_URLS.replace('!!!!', str(year))
            self.year_weekend_url[year] = {}
            page = requests.get(url, timeout=5)
            try:
                rows = BeautifulSoup(page.content, "html5lib").find_all('center')[1].find('table').find_all('tr')
            except:
                print ("something went wrong here")

            if rows is not None:
                for row in rows:
                    if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                        element = row.find('a')

                        if element is not None and element.string is not None:
                            self.year_weekend_url[year][element.string.strip()] = self.BASE_URL + element['href']

    def get_weekend_stats(self)
bom = BoxOfficeMojo()
print (bom.year_weekend_url)

