from bs4 import BeautifulSoup as BS
import requests

url = 'https://www.gammatest.net/course/python/'
r = requests.get(url)
soup = BS(r.content, 'html.parser')
print(soup.a)
