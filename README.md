Box Office Mojo Python API
=============
A basic and simple web scrapper to provide a python API for box office mojo.

It supports getting box office statistics of a film, the latest openning weekend, a specific openning weekend that box office mojo tracks
(from 1982 to 2018). It also writes data to file, and supports reading from file instead of re-scraping every time.

Proxies are being added.

### Pre-req
```
json
BeautifulSoup
requests
html5lib
```

### USAGE 

```python
import boxofficemojo as bom

bom = bom.BoxOfficeMojo()

print (bom.get_movie_stats_by_name('black panther'))

print (bom.get_latest_weekend_stats())

print (bom.get_specific_weekend_stats("2018/08/03")) #Note: date must be in this format and the friday of that weekend

```

the output would be 

Movie
```javascript
[{
    'title': 'Black Panther (2018)',
    'overview': {
        'domestic': '$700,059,566',
        'international': '$646,853,595',
        'worldwide': '$1,346,913,161',
        'openning': '$202,003,951'
    },
    'players': {
        'Director': ['Ryan Coogler'],
        'Actors': ['Chadwick Boseman', "Lupita Nyong'o", 'Michael B. Jordan', 'Angela Bassett', 'Martin Freeman', 'Forest Whitaker', 'Andy Serkis', 'Sterling K. Brown'],
        'Producer': ['Kevin Feige'],
        'Cinematographer': ['Rachel Morrison'],
        'Composer': ['Ludwig Goransson']
    },
    'Distributor': 'Buena Vista',
    'Release Date': 'February 16, 2018',
    'Genre': 'Action / Adventure',
    'Runtime': '2 hrs. 20 min.',
    'MPAA Rating': 'PG-13',
    'Production Budget': 'N/A',
    'weekends': [{
        'Feb 16–18': {
            'rank': '1',
            'gross': '$202,003,951',
            'change': '-',
            'theatres': '4,020',
            'deltaTheatre': '-',
            'avg': '$50,250',
            'gross_to_date': '$202,003,951',
            'week': '1'
        }
    }]
}, {
    'title': 'Black Panthers: Vanguard of the Revolution (2015)',
    'overview': {
        'domestic': '$516,893',
        'international': '$67,216',
        'worldwide': '$584,109',
        'openning': '$20,215'
    },
    'players': {},
    'Distributor': 'PBS Distribution',
    'Release Date': 'September 2, 2015',
    'Genre': 'Documentary',
    'Runtime': '1 hrs. 53 min.',
    'MPAA Rating': 'Unrated',
    'Production Budget': 'N/A',
    'weekends': [{
        'Sep 4–6': {
            'rank': '62',
            'gross': '$20,215',
            'change': '-',
            'theatres': '1',
            'deltaTheatre': '-',
            'avg': '$20,215',
            'gross_to_date': '$28,580',
            'week': '1'
        }
    }]
}]
```

Latest Weekend Stats
```javascript
[{
    'Bohemian Rhapsody': {
        'this week': '1',
        'last week': 'N',
        'studio': 'Fox',
        'gross': '$51,061,119',
        '% change': '-',
        'theatre count': '4,000',
        'theatre change': '-',
        'average': '$12,765',
        'total gross': '$51,061,119',
        'budget': '$52',
        'week #': '1'
    }
}, {
    'The Nutcracker and the Four Realms': {
        'this week': '2',
        'last week': 'N',
        'studio': 'BV',
        'gross': '$20,352,491',
        '% change': '-',
        'theatre count': '3,766',
        'theatre change': '-',
        'average': '$5,404',
        'total gross': '$20,352,491',
        'budget': '$120',
        'week #': '1'
    }
}, {
    "Nobody's Fool": {
        'this week': '3',
        'last week': 'N',
        'studio': 'Par.',
        'gross': '$13,743,111',
        '% change': '-',
        'theatre count': '2,468',
        'theatre change': '-',
        'average': '$5,569',
        'total gross': '$13,743,111',
        'budget': '$19',
        'week #': '1'
    }
}, {
    'A Star is Born (2018)': {
        'this week': '4',
        'last week': '2',
        'studio': 'WB',
        'gross': '$11,003,083',
        '% change': '-21.6%',
        'theatre count': '3,431',
        'theatre change': '-473',
        'average': '$3,207',
        'total gross': '$165,537,649',
        'budget': '$36',
        'week #': '5'
    }
}, {
    'Halloween (2018)': {
        'this week': '5',
        'last week': '1',
        'studio': 'Uni.',
        'gross': '$10,830,865',
        '% change': '-65.5%',
        'theatre count': '3,775',
        'theatre change': '-215',
        'average': '$2,869',
        'total gross': '$150,224,570',
        'budget': '$10',
        'week #': '3'
    }
}]
```

Specific Weekend Stats
```javascript
[{
    'Crazy Rich Asians': {
        'this week': '1',
        'last week': '1',
        'studio': 'WB',
        'gross': '$28,576,222',
        '% change': '+15.2%',
        'theatre count': '3,865',
        'theatre change': '+339',
        'average': '$7,394',
        'total gross': '$117,303,610',
        'budget': '$30',
        'week #': '3'
    }
}, {
    'The Meg': {
        'this week': '2',
        'last week': '2',
        'studio': 'WB',
        'gross': '$13,816,467',
        '% change': '+7.8%',
        'theatre count': '3,761',
        'theatre change': '-270',
        'average': '$3,674',
        'total gross': '$123,802,883',
        'budget': '$130',
        'week #': '4'
    }
}, {
    'Mission: Impossible - Fallout': {
        'this week': '3',
        'last week': '4',
        'studio': 'Par.',
        'gross': '$9,315,171',
        '% change': '+15.2%',
        'theatre count': '2,639',
        'theatre change': '-413',
        'average': '$3,530',
        'total gross': '$206,661,700',
        'budget': '$178',
        'week #': '6'
    }
}, {
    'Operation Finale': {
        'this week': '4',
        'last week': 'N',
        'studio': 'MGM',
        'gross': '$7,874,583',
        '% change': '-',
        'theatre count': '1,818',
        'theatre change': '-',
        'average': '$4,331',
        'total gross': '$9,601,678',
        'budget': '$24',
        'week #': '1'
    }
}, {
    'Searching': {
        'this week': '5',
        'last week': '22',
        'studio': 'SGem',
        'gross': '$7,615,035',
        '% change': '+1,858.8%',
        'theatre count': '1,207',
        'theatre change': '+1,198',
        'average': '$6,309',
        'total gross': '$8,123,515',
        'budget': '-',
        'week #': '2'
    }
}]
```

### Note
This is extremenly basic and is a work in process.
