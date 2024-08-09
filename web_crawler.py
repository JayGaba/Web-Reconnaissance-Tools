import bs4
import requests, os, sys
from urllib.parse import urljoin


domain = sys.argv[1]

content_list = []

with open(f'recon/{domain}/crawler_output', 'w') as file:
    pass


def request(url):
    try:
        html = requests.get(url, allow_redirects=False, timeout=2)
        return html.content
    except:
        return ''

def crawl(url):
    try:
        html = request(url)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        for a in soup.find_all('a', href=True):
            link = urljoin(url, a['href'])
            if '#' in link:
                link = link.split('#')[0]
                
            if link not in content_list and domain in link:
                content_list.append
                print(f"[+] Found the url : {link}")
                with open(f"recon/{domain}/crawler_output", 'a') as file:
                    file.write(link + '\n')
                crawl(link)
                
    except KeyboardInterrupt:
        exit(0)
        
        


with open(f'recon/{domain}/subdomains', 'r') as file:
    subdomains = file.read().splitlines()
    for subdomain in subdomains:
        url = f"https://{subdomain}"
        crawl(url)