import requests
from bs4 import BeautifulSoup

def ScrapeSite(link):
    payload = {'api_key': '6862e364e496975c29d80c2920c90cc7', 'url': link}
    r = requests.get('http://api.scraperapi.com', params=payload)
    if r.status_code == 200:
        ScrappedData = r.text
        return ScrappedData
    else:
        ScrappedData = 'Was Not Sucessful'
        return ScrappedData

def extract_text_from(html):
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()
    title_tag = soup.find('title').text
    lines = (line.strip() for line in text.splitlines())
    pagecontent = '\\n'.join(line for line in lines if line)

    return {'title': title_tag,'pagecontent':pagecontent}


