from bs4 import BeautifulSoup
import requests
from movie import *
import json

page_link = "https://www.boxofficemojo.com/movies/?id=jurassicworldsequel.htm"

page_response = requests.get(page_link, timeout=5)

base = "https://www.boxofficemojo.com/"

url = ""

page_content = BeautifulSoup(page_response.content, "html5lib")

a_movie = Movie(page_content)

print (a_movie.json)

