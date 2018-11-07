from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from bs4 import BeautifulSoup
from movie import *
import re
import datetime

class BoxOfficeMojo(object):

    YEAR_START = 1982
    WEEKEND_URLS = "https://www.boxofficemojo.com/weekend/?yr=!!!!&sort=year&order=DESC&p=.htm" 
    BASE_URL = "https://www.boxofficemojo.com"
    months = {'01' : 'Jan', '02' : 'Feb', '03' : 'Mar', '04' : 'Apr', '05' : 'May', '06': 'Jun', '07' : 'Jul', '08' : 'Aug', '09' : 'Sep', '10' : 'Oct', '11' : 'Nov', '12' : 'Dec'}
    correct_date = [5,6,7]

    def __init__(self):
        self.year_weekend_url = {}
        self.latest = None
    
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
        for year in range(2018,2019):
            url = self.WEEKEND_URLS.replace('!!!!', str(year))
            self.year_weekend_url[year] = {}
            page = requests.get(url, timeout=5)
            try:
                rows = BeautifulSoup(page.content, "html5lib").find_all('center')[1].find('table').find_all('tr')
            except:
                print ("something went wrong here")

            if rows is not None and len(rows) > 0:
                self.latest = rows[1].find('a').string.strip()
                for row in rows:
                    if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                        element = row.find('a')

                        if element is not None and element.string is not None:
                            self.year_weekend_url[year][element.string.strip()] = self.BASE_URL + element['href']

    def get_specific_weekend_stats(self, date, limit=5):
        assert isinstance(date, str)
        regular_expession = re.compile('\d{4}/\d{2}/\d{2}')
        if regular_expession.match(date):
            date_list = date.split('/')
            year = date_list[0]
            month = date_list[1]
            day = date_list[2]

            if month not in self.months or int(day) < 0 or int(day) > 31:
                print ("in correct format") 
            
            if int(year) not in self.year_weekend_url:
                print ("year not currently saved")

            given_date = datetime.date(int(year), int(month), int(day))

            if given_date.isoweekday() != 5:
                print ("not correct start of date")
            
            to_check = self.months[month] + ". " + str(int(day))

            for key in self.year_weekend_url[int(year)].keys():
                if to_check in key:
                    url = self.year_weekend_url[int(year)][key]
                    weekend = Weekend(BeautifulSoup(requests.get(url, timeout=5).content, "html5lib"))

                    for i in range(limit):
                        print (weekend.data[i])
                    break
        else:
            print ("incorrect format")

    def get_latest_weekend_stats(self, limit=5):
        latest_url = self.year_weekend_url[2018][self.latest]
        weekend = Weekend(BeautifulSoup(requests.get(latest_url, timeout=5).content, "html5lib"))

        for i in range(limit):
            print (weekend.data[i])

bom = BoxOfficeMojo()
bom.crawl_for_weekend_urls()
# bom.get_latest_weekend_stats()
bom.get_specific_weekend_stats("2018/08/03")

