import requests
from requests.exceptions import HTTPError

# 200 - success
# 300 - redirect
# 400 - client errors
# 500 - server errors

urls = ['https://api.github.com', 'https://api.github.com/invalid']

for url in urls:
    try:
        r = requests.get(url)
        r.raise_for_status()
        x = 10 * (1/0)
    except HTTPError as http_err:
        print(f'Website error: {http_err}')
    except Exception as err:
        print(f'Other error: {err}')


# r = requests.get('https://api.github.com')
# print(r.text)
