import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

#r = requests.get('https://eksisozluk.com/turkiyeden-siktir-olup-gitmek--3843083?p=1',
 #                headers=headers, timeout=(20, 20), verify=False)

def request(page=1):
    request_str = 'https://eksisozluk.com/turkiyeden-siktir-olup-gitmek--3843083?p={}'.format(page)
    return requests.get(request_str,headers=headers, timeout=(20,20), verify=False)