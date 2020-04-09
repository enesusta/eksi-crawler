import requests
import urllib3
from requests.exceptions import HTTPError

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

host='https://eksisozluk.com/almanya--49635'

def request(page=1):
    request_str = host + '?p={}'.format(page)
    print(request_str)
    response = None
    try:
        response = requests.get(request_str,headers=headers, timeout=(20,20), verify=False)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occured: {err}')
    return response