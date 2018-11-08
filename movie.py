import requests
from bs4 import BeautifulSoup

class MovieWeekendEntry(object):

    labels = ["rank", "gross", "change", "theatres", "deltaTheatre", "avg", "gross_to_date", "week"]

    def __init__(self, data):
        assert len(data) == len(self.labels) + 1
        self.json = {}
        data.pop(0)
        for i in range(len(data)):
            self.json[self.labels[i]] = data[i]

class Weekend(object):

    def __init__(self, html):
        assert isinstance(html, BeautifulSoup)
        self.html = html
        self.data = []
        self.extract_data()
    
    def extract_data(self):
        table = self.html.find('table',attrs={'border' : '0', 'cellspacing' : '1', 'cellpadding' : '5'})

        if table is not None:
            rows = table.find_all('tr')

            for row in rows:
                if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                    datas = []
                    elements = row.find_all('td')
                    for element in elements:
                        datas.append(element.find('font').string)
                    self.data.append(WeekendEntry(datas).json)

class WeekendEntry(object):

    labels = ["this week", "last week", "title", "studio", "gross", "% change", "theatre count", "theatre change", "average", "total gross", "budget", "week #"]
    
    def __init__(self, data):
        self.json = {}
        self.json[data[2]] = {}
        assert len(data) == len(self.labels)
        self.fill_data(data)
    
    def fill_data(self, data):
        for i in range(len(data)):
            if i != 2:
                self.json[data[2]][self.labels[i]] = data[i]
        
class Movie(object):

    def __init__(self, html):

        self.json = {}
        assert isinstance(html, BeautifulSoup)
        self.html = html
        self.base = "https://www.boxofficemojo.com/"
        self.extract_data()

    def extract_data(self):
        title = self.html.title.contents[0].replace(" - Box Office Mojo", "")
        self.json["title"] = title

        tds = self.html.findAll('td', attrs={'width' : '35%', 'align' : 'right'})
        total_domestic = tds[0].find('b').contents[0].strip()
        total_international = tds[1].contents[0].strip()
        total_worldwide = tds[2].find('b').contents[0].strip()

        self.json["overview"] = {}
        self.json["players"] = {}
        self.json["overview"]["domestic"] = total_domestic
        self.json["overview"]["international"] = total_international
        self.json["overview"]["worldwide"] = total_worldwide

        boxes = self.html.find_all('div', attrs = {'class': 'mp_box_content'})

        for box in boxes:
            sibling =  box.find_previous_sibling('div', attrs = {'class' : 'mp_box_tab'})

            if sibling is not None:
                name = sibling.string.strip()
                
                if name == "Domestic Summary":          
                    td = box.find('td', attrs = {'align' : 'center'})
                    self.json["overview"]["openning"] = td.find_next('td').string.strip()
                elif name == "The Players":
                    rows = box.find_all('tr')

                    for row in rows:
                        names = row.find_all('font')

                        category = None
                        if len(names) > 0:
                            if names[0].find('font') is None:
                                category = names[0].string.strip().replace(':', '')
                            else:
                                category = names[0].find('font').string.strip().replace(':', '')

                        if category is not None:
                            if category not in self.json["players"]:
                                self.json["players"][category] = []

                            if len(names) > 0:
                                if names[1].string is not None:
                                    if len(names) == 3:
                                        self.json["players"][category].append(names[2].string.strip())
                                    else:
                                        self.json["players"][category].append(names[1].string.strip())
                                else:
                                    for content in names[1].contents:
                                        if content.string is not None:
                                            if content.string != "" and content.string != 'cameo':
                                                self.json["players"][category].append(content.string.strip())

        overview = self.html.find('center')    
        components = overview.findAll('td', attrs={'valign' : 'top'})

        for component in components:
            self.json[component.contents[0].strip().replace(":","")] = component.find('b').string.strip()
        
        nav_tabs = self.html.find('ul', attrs={'class' : 'nav_tabs'})

        for li in nav_tabs.findChildren():
            if li.string == "Weekend":
                url = self.base + li.find('a')['href']
                break

        weekends = requests.get(url, timeout=5)

        weekend_content = BeautifulSoup(weekends.content, "html5lib")

        tables = weekend_content.find_all('table', attrs = {'border' : '0', 'cellspacing' : '0', 'cellpadding' : '5', 'class' : 'chart-wide'})

        if len(tables) > 0:
            rows = tables[-1].find_all('tr')

            self.json["weekends"] = {}

            for row in rows:
                if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                    datas = []
                    elements = row.find_all('td')

                    for element in elements:
                        datas.append(element.find('font').string)
                    
                    date = datas[0]
                    self.json["weekends"][date] = MovieWeekendEntry(datas).json
