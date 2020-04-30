import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import re

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

# url = 'https://www.grc.com/sn/past/2019.htm'
url = 'https://www.grc.com/securitynow.htm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.findAll('a')

target_links = []
regex = r"sn-\d+\.mp3"

# target link : <a href="https://media.grc.com/sn/sn-014.mp3"><img align="left" border="0" height="16" src="/image/speaker-hq.gif" title="RIGHT CLICK and SAVE AS to download a high quality MP3 audio file" width="16"/></a>
for link in links:
    if not link.get('href'):
        continue

    match = re.search(regex, link['href'])

    if match:
        target_links.append(link['href'])

print('Downloading {} files'.format(len(target_links)))

for download_url in target_links:
    download_name = download_url.split('/')[-1]
    urllib.request.urlretrieve(download_url, './download/' + download_name)
    time.sleep(1)
