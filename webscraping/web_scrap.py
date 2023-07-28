# pip3 install beautifulsoup4

# URL to scrape: https://xeno-canto.org/

# import libraries
from bs4 import BeautifulSoup
import requests

url = "https://xeno-canto.org/"
response = requests.get(url)

# Get title of the page
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')
print(title)