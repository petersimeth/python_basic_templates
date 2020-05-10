import requests

url = 'http://www.heise.de'

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }

response = requests.get(url, headers=headers, timeout=3.05)

with requests.get(url) as resp:
    print(resp.status_code)
    print(resp.url)
    html_data = resp.text
    print(html_data)