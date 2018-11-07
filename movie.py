import requests
from bs4 import BeautifulSoup

class MovieWeekendEntry(object):

    def __init__(self, data):
        self.json = {}
        self.json[data[0]] = {}
        self.json[data[0]]["rank"] = data[1]
        self.json[data[0]]["gross"] = data[2]
        self.json[data[0]]["change"] = data[3]
        self.json[data[0]]["theatres"] = data[4]
        self.json[data[0]]["deltaTheatre"] = data[5]
        self.json[data[0]]["avg"] = data[6]
        self.json[data[0]]["gross_to_date"] = data[7]
        self.json[data[0]]["week"] = data[8]

class WeekenEntry(object):

    def __init__(self, html):
        self.html = html
        self.json = {}
    
    def extract_data(self):
        
class Movie(object):

    def __init__(self, html):

        self.json = {}
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
                        category = names[0].string.strip().replace(":", "")

                        if category not in self.json["players"]:
                            self.json["players"][category] = []

                        if names[1].string is not None:
                            self.json["players"][category].append(names[1].string.strip())
                        else:
                            multi_names = names[1].find_all('a')
                            for a_name in multi_names:
                                self.json["players"][category].append(a_name.string)

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

        table = weekend_content.find('table', attrs = {'border' : '0', 'cellspacing' : '0', 'cellpadding' : '5', 'class' : 'chart-wide'})

        rows = table.find_all('tr')

        self.json["weekends"] = []

        for row in rows:
            if row['bgcolor'] is not None and row['bgcolor'] != '#dcdcdc':
                datas = []
                elements = row.find_all('td')

                for element in elements:
                    datas.append(element.find('font').string)
                
                self.json["weekends"].append(MovieWeekendEntry(datas).json)
