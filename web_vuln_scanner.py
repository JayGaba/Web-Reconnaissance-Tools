import requests, sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, init

init()
red = Fore.RED
reset = Fore.RESET

session = requests.Session()
session.headers["User-Agent"] = ""
session.headers["Cookie"] = ""


def get_forms(url):
    soup = BeautifulSoup(session.get(url).content, "html-parser")
    return soup.find_all("form")


def form_details(form):
    detailsOfForm = {}
    try:
        action = form.attrs.get("action").lower()
        method = form.attrs.get("method").lower()

        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            input.append({"type": input_type, "name": input_name, "value": input_value})

        detailsOfForm["action"] = action
        detailsOfForm["method"] = method
        detailsOfForm["inputs"] = inputs
    except:
        pass

    return detailsOfForm


def submit_form(details, url, data, payload=""):
    try:
        url = urljoin(url, details["action"])    
        if details["method"] == "post":
            res = session.post(url, data=data)
        else:
            res = session.get(url, params=data)

    except:
        res = session.get(url)

    return res


def sqli_vuln(res):
    sqli_errors = [
        "you have an error in your sql syntax",
        "quoted string not properly sanitized",
        "unclosed quotation mark",
        "warning: mysql"
    ]

    for error in sqli_errors:
        if error in res.content.decode().lower():
            return True
        else:
            return False

def sqli_scan_url(url ,payload):
    url = urlparse(url)
    query_string = url.query
    pairs = query_string.split('&')
    
    for j in range(len(pairs)):
        pair = [pairs[j].split('=')[0], pairs[j].split('=')[1]+payload]
        pairs[j] = '='.join(pair)  
          
    qs = '&'.join(pairs)
    print("Query string : ", qs)
    modified_url = url.geturl().split('?')[0]+'?'+qs
    res = session.get(modified_url)


def xss_scan_url(url ,payload):
    url = urlparse(url)
    query_string = url.query
    pairs = query_string.split('&')
    
    for j in range(len(pairs)):
        pair = [pairs[j].split('=')[0], pairs[j].split('=')[1]+payload]
        pairs[j] = '='.join(pair)  
          
    qs = '&'.join(pairs)
    print("Query string : ", qs)
    modified_url = url.geturl().split('?')[0]+'?'+qs
    res = session.get(modified_url)
    
    
def sqli_scan(url):
    forms = get_forms(url)
    print(f"[+] Found {len(forms)} forms in {url}")

    if len(forms) == 0:
        return

    for form in forms:
        details = form_details(form)
        sqli_payload_list = ["\'", '\"']

        for payload in sqli_payload_list:
            data = {}
                
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag["name"]] = input_tag["value"] + payload
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = f"test{payload}"
                
            res = submit_form(details, url, data, payload)
            if '?' in url:
                res = sqli_scan_url(url, payload)

            if sqli_vuln(res):
                print(f"{red}[+] SQL Injection found on {url}{reset}")
            else:
                pass


def xss_scan(url):
    forms = get_forms(url)
    print(f"[+] Found {len(forms)} forms in {url}")
    
    if len(forms) == 0:
        return
    
    js_payload = "<Script>alert('XSS')</script>"
    for form in forms:
        details = form_details(form)
        data = {}
        
        for input_tag in details["inputs"]:
            if input_tag["type"] == "hidden" or input_tag["value"]:
                data[input_tag["name"]] = input_tag["value"] + js_payload
            elif input_tag["type"] != "submit":
                data[input_tag["name"]] = f"test{js_payload}"

        res = submit_form(details, url, data, js_payload)

        if '?' in url:
            res = xss_scan_url(url, js_payload)

        if js_payload in res.content.decode():
            print(f"{red}[+] Cross Site Scripting found on {url}{reset}")
        else:
            pass

if __name__ == '__main__':
    domain = sys.argv[1]
    with open(f'recon/{domain}/crawler_output', 'r') as file:
        urls = file.read().splitlines()
        for url in urls:
            sqli_scan(url)
            xss_scan(url)
            