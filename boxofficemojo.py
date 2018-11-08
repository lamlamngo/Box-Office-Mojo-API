from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
from bs4 import BeautifulSoup
from movie import *
import re
import datetime
import json

class BoxOfficeMojo(object):

    YEAR_START = 1982
    WEEKEND_URLS = "https://www.boxofficemojo.com/weekend/?yr=!!!!&sort=year&order=DESC&p=.htm" 
    BASE_URL = "https://www.boxofficemojo.com"
    months = {'01' : 'Jan', '02' : 'Feb', '03' : 'Mar', '04' : 'Apr', '05' : 'May', '06': 'Jun', '07' : 'Jul', '08' : 'Aug', '09' : 'Sep', '10' : 'Oct', '11' : 'Nov', '12' : 'Dec'}
    correct_date = [5,6,7]
    MOVIE_URLS = "https://www.boxofficemojo.com/movies/alphabetical.htm?letter=!!!&p=.htm"

    def __init__(self, movie_read_from_file=False, weekend_read_from_file=False):
        self.year_weekend_url = {}
        self.latest = None
        self.letters = ['NUM']
        for i in range(65,91):
            self.letters.append(chr(i))
        self.movies_url = {}
        self.movie_read = movie_read_from_file
        self.weekend_read = weekend_read_from_file
        self.crawl_movie_urls()
        self.crawl_for_weekend_urls()
    
    def crawl_movie_urls(self):
        if not self.movie_read:
            for letter in self.letters:
                url = self.MOVIE_URLS.replace('!!!', letter)
                print ("working on letter: " + str(letter))
                page = requests.get(url, timeout = 5)
                soup = BeautifulSoup(page.content, "html5lib")
                self.get_all_movie_links_in_page(soup)
                links = self.get_additional_pages(soup)
                for link in links:
                    new_page = requests.get(self.BASE_URL + link, timeout=5)
                    new_soup = BeautifulSoup(new_page.content, "html5lib")
                    self.get_all_movie_links_in_page(new_soup)
            self.dump_to_file(self.movies_url, "movie_links.txt")
        else:
            self.movies_url = self.read_from_file("movie_links.txt")

    def dump_to_file(self,to_dump, filename):
        regular_expession = re.compile('.*.txt')
        if regular_expession.match(filename):
            with open(filename, 'w') as outfile:  
                json.dump(to_dump, outfile)
        else:
            print ("incorrect file format")
    
    def read_from_file(self, filename):
        regular_expression = re.compile('.*.txt')
        if regular_expression.match(filename):
            with open(filename) as json_file:  
                data = json.load(json_file)
                return data
        return None

    def get_all_movie_links_in_page(self, html):
        assert isinstance(html, BeautifulSoup)
        table = html.find('table', attrs = {'border' : '0', 'cellspace' : '1', 'cellpadding' : '7', 'bgcolor' : '#ffffff', 'width' : '100%'})

        if table is not None:
            rows = table.find_all('tr')

            if len(rows) > 0:
                rows.pop(0)
                for row in rows:
                    column = row.find('td').find('a')
                    if column is not None and column['href'] is not None and column.string is not None:
                        self.movies_url[column.string.strip().lower()] = column['href'] 

    def get_additional_pages(self, html):
        assert isinstance (html, BeautifulSoup)

        holders = html.find_all('div', attrs = {'class' : 'alpha-nav-holder'})

        additional_links = []
        for holder in holders:
            links = holder.find_all('a')
            for link in links:
                additional_links.append(link["href"])
        
        return additional_links
    
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
    
    def get_movie_stats_by_name(self, name):
        keys = []
        name = name.lower()
        assert isinstance(name,str)
        to_return = []
        for key in self.movies_url.keys():
            if name in key:
                keys.append(key)
        for key in keys:
            url = self.BASE_URL + self.movies_url[key]
            soup = BeautifulSoup(requests.get(url,timeout=5).content, "html5lib")
            to_return.append(Movie(soup).json)
        return to_return

    def crawl_for_weekend_urls(self):
        if not self.weekend_read:
            for year in range(1982,2019):
                print ("working on " + str(year))
                url = self.WEEKEND_URLS.replace('!!!!', str(year))
                self.year_weekend_url[str(year)] = {}
                page = requests.get(url, timeout=5)
                try:
                    soup = BeautifulSoup(page.content, "html5lib")
                    tables = soup.find_all('table')
                    for table in tables:
                        if table.find_previous_sibling('b') is not None:
                            rows = table.find_all('tr')
                            break
                    row = None
                except Exception as e:
                    print ("something went wrong here")
                    print (e)
                    row = None

                if rows is not None and len(rows) > 0:
                    for row in rows:
                        if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                            element = row.find('a')

                            if element is not None and element.string is not None:
                                self.year_weekend_url[str(year)][element.string.strip()] = self.BASE_URL + element['href']
            self.dump_to_file(self.year_weekend_url, "weekend_urls.txt")
        else:
            self.year_weekend_url = self.read_from_file("weekend_urls.txt")

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
                return []
            
            if year not in self.year_weekend_url:
                print ("year not currently saved")
                return []

            given_date = datetime.date(int(year), int(month), int(day))

            if given_date.isoweekday() != 5:
                print ("not correct start of date")
                return []
            
            to_check = self.months[month] + ". " + str(int(day)) + "–"

            for key in self.year_weekend_url[year].keys():
                if to_check in key:
                    url = self.year_weekend_url[year][key]
                    weekend = Weekend(BeautifulSoup(requests.get(url, timeout=5).content, "html5lib"))

                    to_return = {}
                    to_return[key] = []
                    for i in range(limit):
                        to_return[key].append(weekend.data[i])
                    return to_return
        else:
            print ("incorrect format")
            return []

    def get_latest_weekend_stats(self, limit=5):
        today = datetime.date.today()
        recent_friday = today - datetime.timedelta(days=today.weekday() + 3)
        date = "%d/%s/%s" % (recent_friday.year, str(recent_friday.month).zfill(2), str(recent_friday.day).zfill(2))
        return self.get_specific_weekend_stats(date, limit = limit)


