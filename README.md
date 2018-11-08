Box Office Mojo Python API
=============
A basic and simple web scrapper to provide a python API for box office mojo.

It supports getting box office statistics of a film, the latest openning weekend, a specific openning weekend that box office mojo tracks
(from 1982 to 2018). It also writes data to file, and supports reading from file instead of re-scraping every time.

Proxies are being added.

### Note
This is extremenly basic and is a work in process.
Current does not fully work for movies that span multiple years. (i'm a dumbass and didn't think of that)
Once you have already saved the data to files. You can do `BoxOfficeMojo(movie_read_from_file=True, weekend_read_from_file=True)` to avoid re-scraping the website.

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
    'weekends': {
        'Feb 16–19': {
            'rank': '1',
            'gross': '$242,155,680',
            'change': '-',
            'theatres': '4,020',
            'deltaTheatre': '-',
            'avg': '$60,238',
            'gross_to_date': '$242,155,680',
            'week': '1'
        },
        'Feb 23–25': {
            'rank': '1',
            'gross': '$111,658,835',
            'change': '-44.7%',
            'theatres': '4,020',
            'deltaTheatre': '-',
            'avg': '$27,776',
            'gross_to_date': '$403,613,257',
            'week': '2'
        },
        'Mar 2–4': {
            'rank': '1',
            'gross': '$66,306,935',
            'change': '-40.6%',
            'theatres': '4,084',
            'deltaTheatre': '+64',
            'avg': '$16,236',
            'gross_to_date': '$501,706,972',
            'week': '3'
        },
        'Mar 9–11': {
            'rank': '1',
            'gross': '$40,817,579',
            'change': '-38.4%',
            'theatres': '3,942',
            'deltaTheatre': '-142',
            'avg': '$10,355',
            'gross_to_date': '$561,697,180',
            'week': '4'
        },
        'Mar 16–18': {
            'rank': '1',
            'gross': '$26,650,690',
            'change': '-34.7%',
            'theatres': '3,834',
            'deltaTheatre': '-108',
            'avg': '$6,951',
            'gross_to_date': '$605,027,218',
            'week': '5'
        },
        'Mar 23–25': {
            'rank': '2',
            'gross': '$17,099,618',
            'change': '-35.8%',
            'theatres': '3,370',
            'deltaTheatre': '-464',
            'avg': '$5,074',
            'gross_to_date': '$631,357,854',
            'week': '6'
        },
        'Mar 30–Apr 1': {
            'rank': '3',
            'gross': '$11,486,915',
            'change': '-32.8%',
            'theatres': '2,988',
            'deltaTheatre': '-382',
            'avg': '$3,844',
            'gross_to_date': '$650,923,549',
            'week': '7'
        },
        'Apr 6–8': {
            'rank': '4',
            'gross': '$8,704,968',
            'change': '-24.2%',
            'theatres': '2,747',
            'deltaTheatre': '-241',
            'avg': '$3,169',
            'gross_to_date': '$665,630,708',
            'week': '8'
        },
        'Apr 13–15': {
            'rank': '6',
            'gross': '$5,777,896',
            'change': '-33.6%',
            'theatres': '2,180',
            'deltaTheatre': '-567',
            'avg': '$2,650',
            'gross_to_date': '$674,233,418',
            'week': '9'
        },
        'Apr 20–22': {
            'rank': '8',
            'gross': '$4,932,627',
            'change': '-14.6%',
            'theatres': '1,930',
            'deltaTheatre': '-250',
            'avg': '$2,556',
            'gross_to_date': '$681,374,736',
            'week': '10'
        },
        'Apr 27–29': {
            'rank': '5',
            'gross': '$4,736,428',
            'change': '-4.0%',
            'theatres': '1,650',
            'deltaTheatre': '-280',
            'avg': '$2,871',
            'gross_to_date': '$688,364,917',
            'week': '11'
        },
        'May 4–6': {
            'rank': '7',
            'gross': '$3,254,977',
            'change': '-31.3%',
            'theatres': '1,641',
            'deltaTheatre': '-9',
            'avg': '$1,984',
            'gross_to_date': '$693,235,592',
            'week': '12'
        },
        'May 11–13': {
            'rank': '9',
            'gross': '$2,077,207',
            'change': '-36.2%',
            'theatres': '1,370',
            'deltaTheatre': '-271',
            'avg': '$1,516',
            'gross_to_date': '$696,331,818',
            'week': '13'
        },
        'May 18–20': {
            'rank': '13',
            'gross': '$860,442',
            'change': '-58.6%',
            'theatres': '935',
            'deltaTheatre': '-435',
            'avg': '$920',
            'gross_to_date': '$697,822,227',
            'week': '14'
        },
        'May 25–27': {
            'rank': '14',
            'gross': '$481,106',
            'change': '-44.1%',
            'theatres': '440',
            'deltaTheatre': '-495',
            'avg': '$1,093',
            'gross_to_date': '$698,617,348',
            'week': '15'
        },
        'May 25–28': {
            'rank': '14',
            'gross': '$608,991',
            'change': '-29.2%',
            'theatres': '440',
            'deltaTheatre': '-495',
            'avg': '$1,384',
            'gross_to_date': '$698,745,233',
            'week': '15'
        },
        'Jun 1–3': {
            'rank': '19',
            'gross': '$246,901',
            'change': '-48.7%',
            'theatres': '284',
            'deltaTheatre': '-156',
            'avg': '$869',
            'gross_to_date': '$699,129,850',
            'week': '16'
        },
        'Jun 8–10': {
            'rank': '25',
            'gross': '$138,693',
            'change': '-43.8%',
            'theatres': '186',
            'deltaTheatre': '-98',
            'avg': '$746',
            'gross_to_date': '$699,389,760',
            'week': '17'
        },
        'Jun 15–17': {
            'rank': '27',
            'gross': '$144,983',
            'change': '+4.5%',
            'theatres': '146',
            'deltaTheatre': '-40',
            'avg': '$993',
            'gross_to_date': '$699,613,337',
            'week': '18'
        },
        'Jun 22–24': {
            'rank': '31',
            'gross': '$75,725',
            'change': '-47.8%',
            'theatres': '115',
            'deltaTheatre': '-31',
            'avg': '$658',
            'gross_to_date': '$699,747,193',
            'week': '19'
        },
        'Jun 29–Jul 1': {
            'rank': '43',
            'gross': '$32,424',
            'change': '-57.2%',
            'theatres': '80',
            'deltaTheatre': '-35',
            'avg': '$405',
            'gross_to_date': '$699,817,122',
            'week': '20'
        },
        'Jul 6–8': {
            'rank': '42',
            'gross': '$31,112',
            'change': '-4.0%',
            'theatres': '52',
            'deltaTheatre': '-28',
            'avg': '$598',
            'gross_to_date': '$699,875,819',
            'week': '21'
        },
        'Jul 13–15': {
            'rank': '50',
            'gross': '$13,859',
            'change': '-55.5%',
            'theatres': '28',
            'deltaTheatre': '-24',
            'avg': '$495',
            'gross_to_date': '$699,900,852',
            'week': '22'
        },
        'Jul 20–22': {
            'rank': '52',
            'gross': '$25,445',
            'change': '+83.6%',
            'theatres': '154',
            'deltaTheatre': '+126',
            'avg': '$165',
            'gross_to_date': '$699,932,307',
            'week': '23'
        },
        'Jul 27–29': {
            'rank': '75',
            'gross': '$2,501',
            'change': '-90.2%',
            'theatres': '15',
            'deltaTheatre': '-139',
            'avg': '$167',
            'gross_to_date': '$699,954,935',
            'week': '24'
        },
        'Aug 3–5': {
            'rank': '44',
            'gross': '$37,389',
            'change': '+1,395%',
            'theatres': '25',
            'deltaTheatre': '+10',
            'avg': '$1,496',
            'gross_to_date': '$700,006,415',
            'week': '25'
        }
    }
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
    'weekends': {
        'Sep 4–7': {
            'rank': '56',
            'gross': '$27,245',
            'change': '-',
            'theatres': '1',
            'deltaTheatre': '-',
            'avg': '$27,245',
            'gross_to_date': '$35,800',
            'week': '1'
        },
        'Sep 11–13': {
            'rank': '56',
            'gross': '$39,865',
            'change': '+97.2%',
            'theatres': '3',
            'deltaTheatre': '+2',
            'avg': '$13,288',
            'gross_to_date': '$86,167',
            'week': '2'
        },
        'Sep 18–20': {
            'rank': '49',
            'gross': '$46,985',
            'change': '+17.9%',
            'theatres': '8',
            'deltaTheatre': '+5',
            'avg': '$5,873',
            'gross_to_date': '$151,282',
            'week': '3'
        },
        'Sep 25–27': {
            'rank': '49',
            'gross': '$47,032',
            'change': '+0.1%',
            'theatres': '10',
            'deltaTheatre': '+2',
            'avg': '$4,703',
            'gross_to_date': '$219,446',
            'week': '4'
        },
        'Oct 2–4': {
            'rank': '47',
            'gross': None,
            'change': '+8.5%',
            'theatres': '12',
            'deltaTheatre': '+2',
            'avg': '$4,254',
            'gross_to_date': None,
            'week': '5'
        },
        'Oct 9–11': {
            'rank': '46',
            'gross': '$47,113',
            'change': '-7.7%',
            'theatres': '12',
            'deltaTheatre': '-',
            'avg': '$3,926',
            'gross_to_date': '$370,651',
            'week': '6'
        },
        'Oct 16–18': {
            'rank': '56',
            'gross': '$21,530',
            'change': '-54.3%',
            'theatres': '11',
            'deltaTheatre': '-1',
            'avg': '$1,957',
            'gross_to_date': '$418,408',
            'week': '7'
        },
        'Oct 23–25': {
            'rank': '94',
            'gross': '$1,478',
            'change': '-93.1%',
            'theatres': '12',
            'deltaTheatre': '+1',
            'avg': '$123',
            'gross_to_date': '$448,851',
            'week': '8'
        },
        'Oct 30–Nov 1': {
            'rank': '72',
            'gross': '$6,852',
            'change': '+364%',
            'theatres': '8',
            'deltaTheatre': '-4',
            'avg': '$857',
            'gross_to_date': '$468,524',
            'week': '9'
        },
        'Nov 6–8': {
            'rank': '79',
            'gross': '$4,414',
            'change': '-35.6%',
            'theatres': '5',
            'deltaTheatre': '-3',
            'avg': '$883',
            'gross_to_date': '$482,396',
            'week': '10'
        }
    }
}]
```

Latest Weekend Stats
```javascript
{
    'Nov. 2–4': [{
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
}
```

Specific Weekend Stats
```javascript
{
    'Aug. 3–5': [{
        'Mission: Impossible - Fallout': {
            'this week': '1',
            'last week': '1',
            'studio': 'Par.',
            'gross': '$35,323,815',
            '% change': '-42.3%',
            'theatre count': '4,395',
            'theatre change': '+9',
            'average': '$8,037',
            'total gross': '$124,811,186',
            'budget': '$178',
            'week #': '2'
        }
    }, {
        "Disney's Christopher Robin": {
            'this week': '2',
            'last week': 'N',
            'studio': 'BV',
            'gross': '$24,585,139',
            '% change': '-',
            'theatre count': '3,602',
            'theatre change': '-',
            'average': '$6,825',
            'total gross': '$24,585,139',
            'budget': '-',
            'week #': '1'
        }
    }, {
        'The Spy Who Dumped Me': {
            'this week': '3',
            'last week': 'N',
            'studio': 'LGF',
            'gross': '$12,103,043',
            '% change': '-',
            'theatre count': '3,111',
            'theatre change': '-',
            'average': '$3,890',
            'total gross': '$12,103,043',
            'budget': '$40',
            'week #': '1'
        }
    }, {
        'Mamma Mia! Here We Go Again': {
            'this week': '4',
            'last week': '2',
            'studio': 'Uni.',
            'gross': '$9,003,030',
            '% change': '-40.4%',
            'theatre count': '3,359',
            'theatre change': '-155',
            'average': '$2,680',
            'total gross': '$91,247,580',
            'budget': '$75',
            'week #': '3'
        }
    }, {
        'The Equalizer 2': {
            'this week': '5',
            'last week': '3',
            'studio': 'Sony',
            'gross': '$8,755,907',
            '% change': '-37.5%',
            'theatre count': '2,725',
            'theatre change': '-663',
            'average': '$3,213',
            'total gross': '$79,812,172',
            'budget': '$62',
            'week #': '3'
        }
    }]
}
```
