import urllib3
import re

def scraper(website):
    
    #get HTML
    http = urllib3.PoolManager()
    r = http.request('GET', website)
    page = r.data.decode('utf-8')
    
    #get all links on page
    links = re.findall(r'a href="https?:\/\/(\S+)"', page)
    
    return links



