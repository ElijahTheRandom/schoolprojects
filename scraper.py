from bs4 import BeautifulSoup
import urllib.request

def wikipediascraper(query):
    query = "_".join(query)
    data = urllib.request.urlopen("https://en.wikipedia.org/wiki/{}".format(query))
    soup = BeautifulSoup(data, 'html.parser')

    for paragraph in soup.find_all('p'):
        if paragraph.b:
            return paragraph.get_text(), query
    
    return "Not Found, Try Something Else"

